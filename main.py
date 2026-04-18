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

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)

