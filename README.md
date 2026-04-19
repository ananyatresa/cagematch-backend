# CageMatch — Backend

FastAPI backend for CageMatch. Handles authentication, movie data from TMDB and user data in Firestore.

## Tech Stack

- Python 3, FastAPI, Uvicorn
- Firebase Admin SDK (auth token verification, Firestore)
- TMDB API (movie data, trailers, OTT providers, cast)
- Pydantic (request/response models)

## Getting Started

```bash
pip install -r requirements.txt
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

## Environment Variables

```
TMDB_API_KEY and FIREBASE_CREDENTIALS
```

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/cagematch/sign_up` | Create user document in Firestore |
| GET | `/cagematch/get_movies_by_genre` | Fetch Nick Cage filmography grouped by genre |
| POST | `/cagematch/get_movie_details` | Full movie details, trailer, cast, OTT, watchlist status |
| GET | `/cagematch/get_user_watchlist` | Fetch user's watchlisted movies |
| POST | `/cagematch/add_to_watchlist` | Toggle a movie in/out of watchlist |
| POST | `/cagematch/like_movie` | Like or dislike a movie |

All endpoints require a Firebase ID token as `Authorization: Bearer <token>`.

## Project Structure

```
controller/       # Route definitions
service/          # Business logic (movie_service.py, user_service.py)
model/            # Pydantic request/response DTOs
firebase_utils/   # Firebase Admin SDK init
utils/            # JWT verification, config helpers
config.yaml       # Timezone → country code mappings for OTT providers
```

## Key Design Notes

- Movie data from TMDB is cached in-memory for 24 hours to reduce API calls.
- OTT provider availability is resolved per user timezone using `config.yaml`.
- Watchlist and like/dislike state is stored as arrays on the Firestore user document.

## Deployment

Deployed on Render.

## Future Enhancements

- Paginate `get_movies_by_genre` for faster initial load
- Persist movie detail cache to Firestore or Redis to survive server restarts
