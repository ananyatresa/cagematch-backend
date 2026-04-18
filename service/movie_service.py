import os
import time
from collections import defaultdict

import requests
from fastapi import HTTPException

from firebase_utils.firebase_config import db
from model.movie_req_res import MovieResponse, MovieItem, MovieDetailsResponse
from utils.util_methods import read_config


class MovieService:
    def __init__(self, logger):
        self.logger = logger
        self.config = read_config()
        self.tmdb_api_key = os.getenv('TMDB_API_KEY')
        self.tmdb_base_url = "https://api.themoviedb.org/3"
        self.cage_id = 2963
        self.genre_cache = None
        self.genre_cache_time = 0
        self.movie_cache = None
        self.movie_cache_time = 0
        self.movie_details_cache = {}
        self.cache_ttl = 60 * 60 * 24  # 24 hours cache TTL

    def get_genre_lookup(self):
        # Return cached genre list if still valid
        if self.genre_cache and (time.time() - self.genre_cache_time) < self.cache_ttl:
            return self.genre_cache

        url = f"{self.tmdb_base_url}/genre/movie/list?api_key={self.tmdb_api_key}"
        response = requests.get(url)
        genres = response.json().get("genres", [])
        self.genre_cache = {g["id"]: g["name"] for g in genres}
        self.genre_cache_time = time.time()
        return self.genre_cache

    def get_movies_by_genre(self):
        try:
            self.logger.info(f"Fetching movies by genre..")
            # Return cached movie data if still valid
            if self.movie_cache and (time.time() - self.movie_cache_time) < self.cache_ttl:
                return self.movie_cache

            url = f"{self.tmdb_base_url}/person/{self.cage_id}/movie_credits?api_key={self.tmdb_api_key}"
            response = requests.get(url)
            movies = response.json().get("cast", [])

            genre_lookup = self.get_genre_lookup()
            genre_map = defaultdict(list)

            for movie in movies:
                if not movie.get("genre_ids") or not movie.get("poster_path"):
                    continue

                # Add TMDB image URL prefix
                img_full_url = f"https://image.tmdb.org/t/p/w500{movie['poster_path']}"

                movie_item = MovieItem(
                    movie_id=movie["id"],
                    title=movie["original_title"],
                    release_date=movie.get("release_date", "N/A"),
                    score=movie.get("popularity", 0),
                    img_url=img_full_url,
                    duration="1 hr 55 mins"
                )

                for genre_id in movie["genre_ids"]:
                    genre_name = genre_lookup.get(genre_id, "Unknown")
                    genre_map[genre_name].append(movie_item)

            result = {"result": [MovieResponse(genre=k, movies=v) for k, v in genre_map.items()]}

            self.movie_cache = result
            self.movie_cache_time = time.time()

            return result
        except Exception as e:
            self.logger.info(f"Error while fetching movies by genre API failed: {e}")
            raise HTTPException(
                status_code=500,
                detail=f"Error while fetching movies by genre API: {e}"
            )

    def get_movie_details(self, movie_req, token):
        """
        Fetch detailed info about a movie by its TMDB ID.
        Uses caching to avoid repeated TMDB calls.
        """
        movie_id = movie_req.movie_id
        user_timezone = movie_req.user_timezone
        user_id = token["uid"]

        user_data = db.collection("users").document(user_id).get().to_dict()

        # Check cache if available
        cached_data = self.movie_details_cache.get(movie_id)
        if cached_data and (time.time() - cached_data["time"]) < self.cache_ttl:
            return {"result": cached_data["data"]}

        # Call TMDB Movie Details API
        movie_url = f"{self.tmdb_base_url}/movie/{movie_id}?api_key={self.tmdb_api_key}&append_to_response=credits,videos"
        response = requests.get(movie_url)

        if response.status_code != 200:
            raise HTTPException(status_code=404, detail="Movie not found")

        movie = response.json()

        available_on = self.fetch_ott_providers(movie_id, user_timezone)
        trailer_url = self.fetch_trailer(movie)
        movie_cast = self.fetch_cast(movie)
        is_watchlist = True if movie_id in user_data.get('watchlist') else False

        return {
            "result": MovieDetailsResponse(movie_id=movie["id"],
                                           title=movie.get("original_title", "N/A"),
                                           release_date=movie.get("release_date", "Unknown"),
                                           language=movie.get("original_language", "en").upper(),
                                           popularity=movie.get("popularity", ""),
                                           duration=f"{movie.get("runtime", 0)} mins",
                                           score=movie.get("popularity", ''),
                                           img_url=f"https://image.tmdb.org/t/p/w500{movie['poster_path']}",
                                           plot=movie.get("overview", ""),
                                           maturity="PG-13" if movie.get("adult") else "U/A",
                                           trailer_url=trailer_url,
                                           cast=movie_cast,
                                           available_on=available_on,
                                           is_watchlist=is_watchlist)
        }

    def fetch_ott_providers(self, movie_id, user_timezone):
        country_code = self.config['timezones'].get(user_timezone, 'Asia/Kolkata')
        available_on = []

        providers_url = f"{self.tmdb_base_url}/movie/{movie_id}/watch/providers?api_key={self.tmdb_api_key}"
        providers_resp = requests.get(providers_url)

        if providers_resp.status_code == 200:
            data = providers_resp.json().get("results", {})
            region_data = data.get(country_code) or data.get("IN")
            if region_data:
                for key in ["flatrate", "rent", "buy"]:
                    if key in region_data:
                        available_on = [p["provider_name"] for p in region_data[key]]
                        break
        return available_on

    def fetch_trailer(self, movie):
        trailer_url = ''
        videos = movie.get("videos", {}).get("results", [])
        for v in videos:
            if v["site"] == "YouTube" and v["type"] == "Trailer":
                trailer_url = f"https://www.youtube.com/watch?v={v['key']}"
                break
        return trailer_url

    def fetch_cast(self, movie):
        # Extract top 10 cast
        cast_data = movie.get("credits", {}).get("cast", [])
        cast = [c["name"] for c in cast_data[:5]]
        return cast
