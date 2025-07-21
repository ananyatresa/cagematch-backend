from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from fastapi import status

from database import get_db
from model.movie_req_res import MovieDetailsRequest
from model.user_req_res import SignUpRequest, LoginRequest
from service.movie_service import MovieService
from service.user_service import UserService
from utils.jwt_handler import verify_token
from utils.utility import read_config

router = APIRouter(prefix="/cagematch")
config = read_config()


@router.post("/sign_up", status_code=status.HTTP_201_CREATED)
def sign_up(req: SignUpRequest, db: Session = Depends(get_db)):
    service = UserService(config=config, db=db)
    return service.sign_up(req)


@router.post("/login")
def login(req: LoginRequest, db: Session = Depends(get_db)):
    service = UserService(config=config, db=db)
    return service.login_user(req)


@router.get("/get_movies_by_genre")
def get_movies_by_genre(user=Depends(verify_token), db: Session = Depends(get_db)):
    service = MovieService(config=config, db=db)
    return service.get_movies_by_genre()


@router.post("/get_movie_details")
def get_movie_details(mov_req: MovieDetailsRequest, user=Depends(verify_token), db: Session = Depends(get_db)):
    service = MovieService(config=config, db=db)
    return service.get_movie_details(mov_req)
