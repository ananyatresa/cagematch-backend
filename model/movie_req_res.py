from typing import List, Dict, Optional

from pydantic import BaseModel


class MovieItem(BaseModel):
    movie_id: int
    title: str
    release_date: Optional[str]
    score: Optional[float]
    img_url: Optional[str]
    duration: Optional[str]


class MovieResponse(BaseModel):
    genre: str
    movies: List[MovieItem]


class MovieDetailsRequest(BaseModel):
    movie_id: int
    user_timezone: str


class MovieDetailsResponse(MovieItem):
    movie_id: int
    trailer_url: str
    maturity: str
    plot: str
    cast: List[str]
    available_on: List[str]
    language: str
    popularity: Optional[float]
    is_watchlist: bool
