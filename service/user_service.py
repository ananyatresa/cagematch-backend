from fastapi import HTTPException
from google.cloud.firestore_v1 import ArrayUnion, ArrayRemove

from firebase_utils.firebase_config import db


class UserService:
    def __init__(self, logger):
        self.logger = logger

    def signup_user(self, req, token):
        self.logger.info("User SignUp logic begins..")
        try:
            user_id = token["uid"]
            email = token["email"]
            user_ref = db.collection("users").document(user_id)
            user_ref.set({
                "username": req.username,
                "email": email,
                "likes": [],
                "dislikes": [],
                "watchlist": []
            })
            return {"result": "User created successfully"}
        except Exception as e:
            self.logger.error(f"User SignUp failed: {e}")
            return {"result": "User SignUp failed!!"}

    def like_movies(self, req, token):
        self.logger.info("User Liked Movies logic begins..")
        try:
            is_liked = req.is_liked
            is_disliked = req.is_disliked
            movie_id = req.movie_id
            user_id = token["uid"]

            user_ref = db.collection("users").document(user_id)
            if is_liked and not is_disliked:
                user_ref.update(
                    {'likes': ArrayUnion([movie_id]),
                     'dislikes': ArrayRemove([movie_id])
                     }
                )
            elif not is_liked and is_disliked:
                user_ref.update(
                    {'dislikes': ArrayUnion([movie_id]),
                     'likes': ArrayRemove([movie_id])
                     }
                )
            elif not is_liked and not is_disliked:
                user_ref.update(
                    {'dislikes': ArrayRemove([movie_id]),
                     'likes': ArrayRemove([movie_id])
                     }
                )
            return {"result": "success"}
        except Exception as e:
            self.logger.error(f"User Like failed: {e}")
            return {"result": "User Like failed!!"}

    def add_to_watchlist(self, req, token):
        self.logger.info("Add to watchlist logic begins..")
        try:
            watchlist_toggle = req.watchlist_toggle
            movie_id = req.movie_id
            user_id = token["uid"]

            user_ref = db.collection("users").document(user_id)
            if watchlist_toggle:
                user_ref.update({'watchlist': ArrayUnion([movie_id])})
            else:
                user_ref.update({'watchlist': ArrayRemove([movie_id])})
            return
        except Exception as e:
            self.logger.error(f"Add to watchlist failed: {e}")
            raise HTTPException(status_code=500, detail="Watchlist update failed")


