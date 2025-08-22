from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.auth import LoginRequest, SignupRequest, TokenPair
from app.core.db import get_db
from app.core.security import get_password_hash, create_access_token, create_refresh_token
from app.services.auth import authenticate_user
from app.models.user import User

router = APIRouter()

@router.post("/signup", response_model=TokenPair)
def signup(body: SignupRequest, db: Session = Depends(get_db)):
    exists = db.query(User).filter(User.email == body.email).first()
    if exists:
        raise HTTPException(status_code=400, detail="Email already registered")
    user = User(email=body.email, password_hash=get_password_hash(body.password), is_admin=False)
    db.add(user)
    db.commit()
    access = create_access_token(body.email)
    refresh = create_refresh_token(body.email)
    return TokenPair(access_token=access, refresh_token=refresh)

@router.post("/login", response_model=TokenPair)
def login(body: LoginRequest, db: Session = Depends(get_db)):
    user = authenticate_user(db, body.email, body.password)
    if not user:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    access = create_access_token(user.email)
    refresh = create_refresh_token(user.email)
    return TokenPair(access_token=access, refresh_token=refresh)
