from collections import defaultdict

from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from db_models.movie_model import Movie
from model.movie_req_res import MovieResponse, MovieItem


class MovieService:
    def __init__(self, config, db: Session):
        self.get_config = config
        self.db = db

    def get_movies_by_genre(self):
        movies = self.db.query(Movie).all()
        genre_map = defaultdict(list)

        for movie in movies:
            movie_item = MovieItem(title=movie.title, release_date=str(movie.release_date), score=movie.score,
                                   img_url=movie.img_url, duration=movie.duration)

            for genre in movie.genres:
                genre_map[genre].append(movie_item)

        return {"result": [MovieResponse(genre=k, movies=v) for k, v in genre_map.items()]}
