from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import func, case
from typing import List
from app.core.db import get_db
from app.schemas.scoreboard import ScoreboardEntry
from app.models.user import User
from app.models.challenge import Submission, Challenge

router = APIRouter()

@router.get("/", response_model=List[ScoreboardEntry])
def top(db: Session = Depends(get_db)):
    q = (
        db.query(
            User.id.label("user_id"),
            User.email.label("email"),
            func.coalesce(func.sum(case((Submission.correct == True, Challenge.points), else_=0)), 0).label("score")
        )
        .outerjoin(Submission, Submission.user_id == User.id)
        .outerjoin(Challenge, Challenge.id == Submission.challenge_id)
        .group_by(User.id)
        .order_by(func.coalesce(func.sum(case((Submission.correct == True, Challenge.points), else_=0)), 0).desc())
        .limit(100)
    )
    return [ScoreboardEntry(user_id=r.user_id, email=r.email, score=int(r.score or 0)) for r in q]
