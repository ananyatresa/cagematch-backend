from fastapi import FastAPI
import uvicorn
import os
import yaml
from fastapi.middleware.cors import CORSMiddleware

from controller import movie_controller

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # React frontend
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

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)

