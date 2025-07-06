from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import get_db
from model.movie_req_res import MovieRequest
from service.movie_service import MovieService
from utils.utility import read_config

router = APIRouter(prefix="/cage_match")
config = read_config()

@router.post("/get_movie")
def get_movie(req: MovieRequest, db: Session = Depends(get_db)):
    service = MovieService(config=config, db=db)  # ✅ Pass both
    return service.get_movie(req)
