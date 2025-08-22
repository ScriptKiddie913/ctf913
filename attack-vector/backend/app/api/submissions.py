from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.db import get_db
from app.schemas.submission import SubmitFlagRequest, SubmissionOut
from app.services.auth import get_current_user
from app.utils.crypto import hash_flag
from app.models.challenge import Challenge, Submission
from typing import List

router = APIRouter()

@router.post("/", response_model=SubmissionOut)
def submit_flag(body: SubmitFlagRequest, db: Session = Depends(get_db), user=Depends(get_current_user)):
    challenge = db.query(Challenge).get(body.challenge_id)
    if not challenge:
        raise HTTPException(status_code=404, detail="Challenge not found")

    # prevent resubmission once solved correctly
    solved = db.query(Submission).filter_by(user_id=user.id, challenge_id=challenge.id, correct=True).first()
    if solved:
        raise HTTPException(status_code=400, detail="Already solved")

    # verify
    correct = (hash_flag(body.flag) == challenge.flag_hash)

    sub = Submission(user_id=user.id, challenge_id=challenge.id, flag_submitted="***", correct=correct)
    db.add(sub); db.commit(); db.refresh(sub)

    if not correct:
        raise HTTPException(status_code=400, detail="Incorrect flag")

    return sub

@router.get("/mine", response_model=List[SubmissionOut])
def my_submissions(db: Session = Depends(get_db), user=Depends(get_current_user)):
    subs = db.query(Submission).filter_by(user_id=user.id).all()
    return subs
