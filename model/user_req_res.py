from pydantic import BaseModel


class SignUpRequest(BaseModel):
    username: str

class LikeRequest(BaseModel):
    movie_id: int
    is_liked: bool
    is_disliked: bool

class WatchListRequest(BaseModel):
    movie_id: int
    watchlist_toggle: bool
