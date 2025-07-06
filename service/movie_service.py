from sqlalchemy.orm import Session

from db_models.movie_model import Movie
from model.movie_req_res import MovieResponse


class MovieService:
    def __init__(self, config, db: Session):
        self.get_config = config
        self.db = db

    def get_movie(self, req):
        mood = req.mood
        matching_movies = self.db.query(Movie).filter(Movie.genres.any(mood)).all()
        movies = [{'name': movie.title, 'image': movie.img_url} for movie in matching_movies]
        return {"result": MovieResponse(mood=mood, movies=movies)}

