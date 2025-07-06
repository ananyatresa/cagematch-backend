import uuid

from sqlalchemy import Column, String, Integer, Date
from sqlalchemy.dialects.postgresql import ARRAY
from database import Base

class Movie(Base):
    __tablename__ = "movies"

    movie_id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    title = Column(String, nullable=False)
    release_date = Column(Date)
    score = Column(Integer)

    img_url = Column(String)
    trailer_url = Column(String)
    duration = Column(String)
    maturity = Column(String)

    genres = Column(ARRAY(String), default=[])
    plot = Column(String)
    cast = Column(ARRAY(String), default=[])
    available_on = Column(ARRAY(String), default=[])
    language = Column(String)
    popularity = Column(ARRAY(String), default=[])
