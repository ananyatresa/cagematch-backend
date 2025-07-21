from collections import defaultdict

from fastapi import HTTPException
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from db_models.movie_model import Movie
from model.movie_req_res import MovieResponse, MovieItem, MovieDetailsResponse


class MovieService:
    def __init__(self, config, db: Session):
        self.get_config = config
        self.db = db

    def get_movies_by_genre(self):
        movies = self.db.query(Movie).all()
        if not movies:
            raise HTTPException(status_code=404, detail="No movies found")
        genre_map = defaultdict(list)

        for movie in movies:
            movie_item = MovieItem(movie_id=movie.movie_id, title=movie.title, release_date=str(movie.release_date), score=movie.score,
                                   img_url=movie.img_url, duration=movie.duration)

            for genre in movie.genres:
                genre_map[genre].append(movie_item)

        return {"result": [MovieResponse(genre=k, movies=v) for k, v in genre_map.items()]}

    def get_movie_details(self, request):
        movie = self.db.query(Movie).filter_by(movie_id=request.movie_id).first()
        if not movie:
            raise HTTPException(status_code=404, detail="Movie not found")

        return {
            "result": MovieDetailsResponse(movie_id=movie.movie_id, title=movie.title, release_date=str(movie.release_date), score=movie.score,
                                           img_url=movie.img_url, duration=movie.duration,
                                           trailer_url=movie.trailer_url,
                                           maturity=movie.maturity, plot=movie.plot, cast=movie.cast,
                                           available_on=movie.available_on, language=movie.language,
                                           popularity=movie.popularity)}
