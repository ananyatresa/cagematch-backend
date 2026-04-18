import json
import os

import firebase_admin
from firebase_admin import credentials, firestore

firebase_config = os.getenv("FIREBASE_KEY")
if firebase_config:
    cred = credentials.Certificate(json.loads(firebase_config))
else:
    raise Exception("Firebase credentials not found")

if not firebase_admin._apps:
    firebase_admin.initialize_app(cred)

db = firestore.client()