from typing import List, Dict, Optional

from pydantic import BaseModel


class MovieItem(BaseModel):
    movie_id: str
    title: str
    release_date: Optional[str]
    score: Optional[int]
    img_url: Optional[str]
    duration: Optional[str]


class MovieResponse(BaseModel):
    genre: str
    movies: List[MovieItem]


class MovieDetailsRequest(BaseModel):
    movie_id: str


class MovieDetailsResponse(MovieItem):
    trailer_url: str
    maturity: str
    plot: str
    cast: List[str]
    available_on: List[str]
    language: str
    popularity: List[str]
