import uuid

from sqlalchemy import Column, String
from sqlalchemy.dialects.postgresql import ARRAY

from database import Base


class User(Base):
    __tablename__= 'users'

    user_id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    username = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    likes = Column(ARRAY(String), default=[])
    dislikes = Column(ARRAY(String), default=[])
    watchlist = Column(ARRAY(String), default=[])