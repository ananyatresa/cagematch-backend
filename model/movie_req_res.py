from typing import List, Dict, Optional

from pydantic import BaseModel


class MovieItem(BaseModel):
    title: str
    release_date: Optional[str]
    score: Optional[int]
    img_url: Optional[str]
    duration: Optional[str]



class MovieResponse(BaseModel):
    genre: str
    movies: List[MovieItem]
