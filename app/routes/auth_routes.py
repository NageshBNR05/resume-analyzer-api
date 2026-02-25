from fastapi import APIRouter, HTTPException
from app.models.user_model import users_db
from app.utils.security import hash_password, verify_password
from jose import jwt
from datetime import datetime, timedelta

router = APIRouter()

SECRET_KEY = "supersecretkey"
ALGORITHM = "HS256"

@router.post("/register")
def register(username: str, password: str):
    if username in users_db:
        raise HTTPException(status_code=400, detail="User already exists")

    hashed = hash_password(password)
    users_db[username] = {"username": username, "password": hashed}
    return {"message": "User registered successfully"}

@router.post("/login")
def login(username: str, password: str):
    user = users_db.get(username)

    if not user or not verify_password(password, user["password"]):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    token_data = {
        "sub": username,
        "exp": datetime.utcnow() + timedelta(minutes=30)
    }

    token = jwt.encode(token_data, SECRET_KEY, algorithm=ALGORITHM)

    return {"access_token": token, "token_type": "bearer"}