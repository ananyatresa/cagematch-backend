import logging
import os

import yaml
from fastapi import APIRouter
from fastapi import status, Request

from model.movie_req_res import MovieDetailsRequest
from model.user_req_res import SignUpRequest, LikeRequest, WatchListRequest
from service.movie_service import MovieService
from service.user_service import UserService
from utils.jwt_handler import verify_bearer_token

router = APIRouter(prefix="/cagematch")
logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s] [%(levelname)s] [%(name)s] %(message)s"
)

user_svc = UserService(logging)
movie_svc = MovieService(logging)


@router.post("/sign_up", status_code=status.HTTP_201_CREATED)
def sign_up(request: Request, signup_req: SignUpRequest):
    token = verify_bearer_token(request.headers)
    return user_svc.signup_user(signup_req, token)


@router.get("/get_movies_by_genre")
def get_movies_by_genre(request: Request):
    token = verify_bearer_token(request.headers)
    return movie_svc.get_movies_by_genre()


@router.post("/get_movie_details")
def get_movie_details(request: Request, mov_req: MovieDetailsRequest):
    token = verify_bearer_token(request.headers)
    return movie_svc.get_movie_details(mov_req, token)


@router.post("/like_movie")
def like_movie(request: Request, like_req: LikeRequest):
    token = verify_bearer_token(request.headers)
    return user_svc.like_movies(like_req, token)


@router.post("/add_to_watchlist")
def watchlist_movie(request: Request, watchlist_req: WatchListRequest):
    token = verify_bearer_token(request.headers)
    return user_svc.add_to_watchlist(watchlist_req, token)
