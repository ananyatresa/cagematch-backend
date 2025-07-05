from fastapi import APIRouter

from model.movie_req_res import MovieRequest
from service.movie_service import MovieService
from utils.utility import read_config

router = APIRouter(prefix="/cage_match")
config = read_config()
movie_service = MovieService(config)



@router.post("/get_movie")
def get_movie(req: MovieRequest):
    return movie_service.get_movie(req)
