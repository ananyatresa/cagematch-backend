from database import engine, Base
from db_models import user_model, movie_model

print("Creating tables...")

Base.metadata.create_all(bind=engine)

print("Tables created successfully in Render DB")
