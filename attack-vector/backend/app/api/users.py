from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.user import UserOut
from app.core.db import get_db
from app.services.auth import get_current_user
from app.models.user import User

router = APIRouter()

@router.get("/me", response_model=UserOut)
def me(user: User = Depends(get_current_user)):
    return user
