from typing import List, Dict

from pydantic import BaseModel


class MovieRequest(BaseModel):
    mood: str


class MovieResponse(MovieRequest):
    movies: List[Dict]
