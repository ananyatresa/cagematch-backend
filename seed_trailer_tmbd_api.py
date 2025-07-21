import requests
from sqlalchemy import create_engine, text
from sqlalchemy.orm import Session

from database import SessionLocal

TMDB_API_KEY = ""
TMDB_BASE_URL = "https://api.themoviedb.org/3"
CAGE_ID = 2963  # Nicolas Cage TMDB person_id

# Create DB session


def get_movie_trailers():
    db: Session = SessionLocal()
    my_movs = ["Adaptation", "National Treasure 2", "Face/Off", "Matchstick Men", "Lord of War","Con Air","Bad Lieutenant: Port of New Orleans","National Treasure","Gone in 60 seconds","The Unbearable Weight of Massive Talent","Mandy","Leaving Las Vegas","Bringing out the Dead","Pig","Vampire's Kiss","Raising Arizona"]
    my_mov = set([mov.lower() for mov in my_movs])

    # Step 1: Get all movies of Nicolas Cage
    credits_url = f"{TMDB_BASE_URL}/person/{CAGE_ID}/movie_credits?api_key={TMDB_API_KEY}"
    response = requests.get(credits_url)
    response.raise_for_status()
    movies = response.json().get("cast", [])
    movies = [mov for mov in movies if mov.get("title").lower() in my_mov]

    for movie in movies:
        title = movie.get("title")
        tmdb_id = movie.get("id")

        # Step 2: Get video (trailer) info
        videos_url = f"{TMDB_BASE_URL}/movie/{tmdb_id}/videos?api_key={TMDB_API_KEY}"
        videos_resp = requests.get(videos_url)
        if videos_resp.status_code != 200:
            continue

        videos = videos_resp.json().get("results", [])
        youtube_trailer = next(
            (v for v in videos if v["site"] == "YouTube" and v["type"] == "Trailer"), None
        )

        if youtube_trailer:
            youtube_url = f"https://www.youtube.com/watch?v={youtube_trailer['key']}"
            print(f"Found trailer for {title}: {youtube_url}")

            # Step 3: Update local DB
            result = db.execute(
                text("UPDATE movies SET trailer_url = :url WHERE title ILIKE :title"),
                {"url": youtube_url, "title": f"%{title}%"}
            )
            db.commit()
            if result.rowcount > 0:
                print(f"✅ Updated: {title}")
            else:
                print(f"⚠️  No match in DB for: {title}")

    db.close()
