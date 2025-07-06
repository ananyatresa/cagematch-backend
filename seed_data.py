from sqlalchemy.orm import Session
from database import SessionLocal
from db_models.user_model import User
from db_models.movie_model import Movie
import datetime


def seed_movies():
    # Create DB session
    db: Session = SessionLocal()

    movie_data = [
        {
            "title": "Adaptation",
            "release_date": datetime.date(2002, 12, 6),
            "score": 91,
            "duration": "1h 55m",
            "maturity": "R",
            "genres": ['oscar', 'weird', 'comedy'],
            "plot": "A screenwriter struggles to adapt a book while dealing with personal insecurities.",
            "cast": ["Nicolas Cage", "Meryl Streep"],
            "available_on": ["Prime Video"],
            "language": "English",
            "popularity": ["cult", "award-winning"],
            "img_url": "https://m.media-amazon.com/images/M/MV5BMmQ1MWMxZjEtNmNmYi00ZGFhLWExZDItODcwNzlmZjg0YzNlXkEyXkFqcGc@._V1_FMjpg_UX1000_.jpg"
        },
        {
            "title": "Bringing out the Dead",
            "release_date": datetime.date(1999, 10, 22),
            "score": 74,
            "duration": "2h 1m",
            "maturity": "R",
            "genres": ['drama'],
            "plot": "A paramedic in NYC battles burnout and haunting memories during night shifts.",
            "cast": ["Nicolas Cage", "Patricia Arquette"],
            "available_on": ["Paramount+"],
            "language": "English",
            "popularity": ["dark-drama"],
            "img_url": "https://m.media-amazon.com/images/M/MV5BNGVjYjU5YzItYTVmMS00ZTUwLTkzMDgtYzI5MGI2MmFkZmQ0XkEyXkFqcGc@._V1_FMjpg_UX1000_.jpg"
        },
        {
            "title": "Leaving Las Vegas",
            "release_date": datetime.date(1995, 10, 27),
            "score": 90,
            "duration": "1h 51m",
            "maturity": "R",
            "genres": ['drama', 'oscar'],
            "plot": "An alcoholic forms a relationship with a sex worker in Las Vegas.",
            "cast": ["Nicolas Cage", "Elisabeth Shue"],
            "available_on": ["Apple TV"],
            "language": "English",
            "popularity": ["oscar", "classic"],
            "img_url": "https://resizing.flixster.com/-XZAfHZM39UwaGJIFWKAE8fS0ak=/v3/t/assets/p17161_p_v8_ah.jpg"
        },
        {
            "title": "Raising Arizona",
            "release_date": datetime.date(1987, 3, 6),
            "score": 85,
            "duration": "1h 34m",
            "maturity": "PG-13",
            "genres": ['comedy'],
            "plot": "An ex-con and his wife kidnap a baby after learning they can’t conceive.",
            "cast": ["Nicolas Cage", "Holly Hunter"],
            "available_on": ["Hulu"],
            "language": "English",
            "popularity": ["coen-brothers", "classic"],
            "img_url": "https://m.media-amazon.com/images/I/81FTrY0BT3L._SY606_.jpg"
        },
        {
            "title": "The Unbearable Weight of Massive Talent",
            "release_date": datetime.date(2022, 4, 22),
            "score": 87,
            "duration": "1h 47m",
            "maturity": "R",
            "genres": ['comedy'],
            "plot": "Nicolas Cage plays himself in a meta comedy about fandom and CIA missions.",
            "cast": ["Nicolas Cage", "Pedro Pascal"],
            "available_on": ["Lionsgate", "Netflix"],
            "language": "English",
            "popularity": ["new", "funny"],
            "img_url": "https://m.media-amazon.com/images/I/91kffE9V8fL._AC_UF1000,1000_QL80_.jpg"
        },
        {
            "title": "Vampire's Kiss",
            "release_date": datetime.date(1989, 6, 2),
            "score": 68,
            "duration": "1h 43m",
            "maturity": "R",
            "genres": ['comedy', 'weird'],
            "plot": "A literary agent believes he's turning into a vampire after a strange encounter.",
            "cast": ["Nicolas Cage", "Maria Conchita Alonso"],
            "available_on": ["Amazon Prime"],
            "language": "English",
            "popularity": ["cult", "weird"],
            "img_url": "https://m.media-amazon.com/images/M/MV5BMTM1MDAyMDYxMV5BMl5BanBnXkFtZTcwNDQwMzc3NA@@._V1_FMjpg_UX1000_.jpg"
        },
        {
            "title": "Con Air",
            "release_date": datetime.date(1997, 6, 6),
            "score": 89,
            "duration": "1h 55m",
            "maturity": "R",
            "genres": ['thriller'],
            "plot": "A parolee tries to get home on a plane full of dangerous convicts.",
            "cast": ["Nicolas Cage", "John Malkovich"],
            "available_on": ["Disney+", "Hotstar"],
            "language": "English",
            "popularity": ["action", "90s"],
            "img_url": "https://resizing.flixster.com/-XZAfHZM39UwaGJIFWKAE8fS0ak=/v3/t/assets/p19439_p_v8_av.jpg"
        },
        {
            "title": "Face/Off",
            "release_date": datetime.date(1997, 6, 27),
            "score": 92,
            "duration": "2h 18m",
            "maturity": "R",
            "genres": ['thriller'],
            "plot": "An FBI agent and a terrorist swap faces in a high-tech chase.",
            "cast": ["Nicolas Cage", "John Travolta"],
            "available_on": ["Netflix", "Paramount+"],
            "language": "English",
            "popularity": ["cult", "sci-fi"],
            "img_url": "https://m.media-amazon.com/images/M/MV5BOGQyOWNmYTgtZWY0NS00NzhjLTg3NmMtMzcwYzQ2OTA2OTJkXkEyXkFqcGc@._V1_FMjpg_UX1000_.jpg"
        },
        {
            "title": "Gone in 60 seconds",
            "release_date": datetime.date(2000, 6, 9),
            "score": 80,
            "duration": "1h 58m",
            "maturity": "PG-13",
            "genres": ['thriller'],
            "plot": "A retired car thief must steal 50 cars in one night to save his brother.",
            "cast": ["Nicolas Cage", "Angelina Jolie"],
            "available_on": ["Disney+", "Hotstar"],
            "language": "English",
            "popularity": ["heist", "car-action"],
            "img_url": "https://m.media-amazon.com/images/M/MV5BMTIwMzExNDEwN15BMl5BanBnXkFtZTYwODMxMzg2._V1_FMjpg_UX1000_.jpg"
        },
        {
            "title": "Bad Lieutenant: Port of New Orleans",
            "release_date": datetime.date(2009, 11, 20),
            "score": 76,
            "duration": "2h 1m",
            "maturity": "R",
            "genres": ['crime'],
            "plot": "A corrupt detective investigates a drug killing while battling addiction.",
            "cast": ["Nicolas Cage", "Eva Mendes"],
            "available_on": ["Amazon Prime"],
            "language": "English",
            "popularity": ["gritty", "noir"],
            "img_url": "https://images.squarespace-cdn.com/content/v1/583c906ebe659429d1106265/f4e1013b-7fd8-4986-8e5f-92206a8b1e19/51SNRejtoNL._RI_SX300_.jpg"
        },
        {
            "title": "Matchstick Men",
            "release_date": datetime.date(2003, 9, 12),
            "score": 83,
            "duration": "1h 56m",
            "maturity": "PG-13",
            "genres": ['crime'],
            "plot": "A con artist discovers he has a teenage daughter while pulling off a long con.",
            "cast": ["Nicolas Cage", "Sam Rockwell"],
            "available_on": ["Peacock"],
            "language": "English",
            "popularity": ["con-artist"],
            "img_url": "https://m.media-amazon.com/images/M/MV5BMjA3NjMyNjIyMF5BMl5BanBnXkFtZTYwOTgzMDI3._V1_.jpg"
        },
        {
            "title": "Lord of War",
            "release_date": datetime.date(2005, 9, 16),
            "score": 85,
            "duration": "2h 2m",
            "maturity": "R",
            "genres": ['crime'],
            "plot": "An arms dealer rises in power while justifying his morality.",
            "cast": ["Nicolas Cage", "Jared Leto"],
            "available_on": ["Hulu", "Netflix"],
            "language": "English",
            "popularity": ["dark", "political"],
            "img_url": "https://d3tvwjfge35btc.cloudfront.net/Assets/66/495/L_p1019749566.jpg"
        },
        {
            "title": "National Treasure",
            "release_date": datetime.date(2004, 11, 19),
            "score": 84,
            "duration": "2h 11m",
            "maturity": "PG",
            "genres": ['mission'],
            "plot": "A historian races to find a legendary treasure hidden in American symbols.",
            "cast": ["Nicolas Cage", "Diane Kruger"],
            "available_on": ["Disney+"],
            "language": "English",
            "popularity": ["adventure"],
            "img_url": "https://images.moviesanywhere.com/7e2320f8ed4e312ffe34dc770a733314/bfe04b95-9f63-4ef8-94d6-ad6d791eb7da.jpg"
        },
        {
            "title": "National Treasure 2",
            "release_date": datetime.date(2007, 12, 21),
            "score": 79,
            "duration": "2h 4m",
            "maturity": "PG",
            "genres": ['mission'],
            "plot": "Ben Gates searches for the mythical City of Gold to clear his family name.",
            "cast": ["Nicolas Cage", "Ed Harris"],
            "available_on": ["Disney+"],
            "language": "English",
            "popularity": ["adventure", "sequel"],
            "img_url": "https://lumiere-a.akamaihd.net/v1/images/p_nationaltreasure2bookofsecrets_19895_8713f371.jpeg"
        },
        {
            "title": "Mandy",
            "release_date": datetime.date(2018, 9, 14),
            "score": 86,
            "duration": "2h 1m",
            "maturity": "R",
            "genres": ['weird', 'horror'],
            "plot": "A man hunts a religious cult in a neon-tinged, ultra-violent nightmare.",
            "cast": ["Nicolas Cage", "Andrea Riseborough"],
            "available_on": ["Shudder"],
            "language": "English",
            "popularity": ["psychedelic", "revenge"],
            "img_url": "https://upload.wikimedia.org/wikipedia/en/9/9a/Mandy_%282018_film%29.png"
        },
        {
            "title": "Pig",
            "release_date": datetime.date(2021, 7, 16),
            "score": 89,
            "duration": "1h 32m",
            "maturity": "R",
            "genres": ['weird'],
            "plot": "A truffle hunter in Oregon searches for his kidnapped pig.",
            "cast": ["Nicolas Cage", "Alex Wolff"],
            "available_on": ["Hulu"],
            "language": "English",
            "popularity": ["emotional", "underdog"],
            "img_url": "https://upload.wikimedia.org/wikipedia/en/e/e2/Pig_poster.jpeg"
        }
    ]

    # 👇 Insert into database if not already there
    for m in movie_data:
        if not db.query(Movie).filter_by(title=m["title"]).first():
            db.add(Movie(
                title=m["title"],
                release_date=m["release_date"],
                score=m["score"],
                img_url=m["img_url"],
                trailer_url="",
                duration=m["duration"],
                maturity=m["maturity"],
                genres=m["genres"],
                plot=m["plot"],
                cast=m["cast"],
                available_on=m["available_on"],
                language=m["language"],
                popularity=m["popularity"]
            ))

    db.commit()
    db.close()

print("All Nicolas Cage movies inserted successfully.")
