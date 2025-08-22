from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import List, Optional
from app.core.db import get_db
from app.schemas.challenge import ChallengeOut
from app.models.challenge import Challenge, Category
from app.services.auth import get_current_user

router = APIRouter()

@router.get("/", response_model=List[ChallengeOut])
def list_challenges(category: Optional[int] = Query(None), storyline: Optional[str] = Query(None), db: Session = Depends(get_db), user=Depends(get_current_user)):
    q = db.query(Challenge)
    if category:
        q = q.filter(Challenge.category_id == category)
    if storyline:
        q = q.filter(Challenge.storyline == storyline)
    # Order OSINT storyline challenges by sequence if present
    q = q.order_by(Challenge.storyline.is_(None), Challenge.sequence.is_(None), Challenge.sequence)
    return q.all()
