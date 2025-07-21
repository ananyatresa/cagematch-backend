from fastapi import FastAPI
import uvicorn
import os
import yaml
from fastapi.middleware.cors import CORSMiddleware

from controller import movie_controller

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "https://cagematch-frontend-sage.vercel.app"],  # React frontend
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(movie_controller.router)


def read_config():
    base_dir = os.path.dirname(os.path.abspath(__file__))

    # Construct the path to the config file
    file_path = os.path.join(base_dir, "config.yaml")

    with open(file_path,'r') as file:
        config = yaml.safe_load(file)
    return config

# For creating tables and inserting seed data - Run once initially for setting up db, tables and data
from database import Base, engine
from db_models import user_model, movie_model
# from seed_data import seed_movies
# from seed_trailer_tmbd_api import get_movie_trailers
# Base.metadata.create_all(bind=engine)
# get_movie_trailers()
#
# Base.metadata.create_all(bind=engine)
# seed_movies()


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)

