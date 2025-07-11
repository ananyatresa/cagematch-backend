import bcrypt
from fastapi import HTTPException
from sqlalchemy.orm import Session

from db_models.user_model import User
from model.user_req_res import SignUpResponse, LoginResponse
from utils.jwt_handler import create_access_token


class UserService:
    def __init__(self, config, db: Session):
        self.get_config = config
        self.db = db

    def sign_up(self, req):
        # Check if user exists:
        if self.db.query(User).filter_by(email=req.email).first():
            raise HTTPException(status_code=409, detail="Email already registered")

        # Hash password before storing
        hashed_pw = bcrypt.hashpw(req.password.encode('utf-8'), bcrypt.gensalt())

        new_user = User(email=req.email, username=req.username, password=hashed_pw.decode('utf-8'))

        self.db.add(new_user)
        self.db.commit()
        self.db.refresh(new_user)

        return SignUpResponse(message="User created successfully", user_id=new_user.user_id)

    def login_user(self, req):
        email = req.email
        password = req.password

        user = self.db.query(User).filter_by(email=email).first()

        if not user:
            raise HTTPException(status_code=401, detail="Invalid credentials")

        if not bcrypt.checkpw(password.encode('utf-8'), user.password.encode('utf-8')):
            raise HTTPException(status_code=401, detail="Invalid credentials")

        # Generate JWT token
        token = create_access_token({
            "user_id": user.user_id,
            "username": user.username
        })

        return LoginResponse(access_token=token, token_type="bearer")


