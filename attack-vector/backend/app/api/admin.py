from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.core.db import get_db
from app.schemas.challenge import ChallengeCreate, ChallengeOut, CategoryOut
from app.models.challenge import Challenge, Category
from app.utils.crypto import hash_flag
from app.services.auth import get_current_admin

router = APIRouter()

@router.post("/categories", response_model=CategoryOut)
def add_category(cat: CategoryOut, db: Session = Depends(get_db), admin=Depends(get_current_admin)):
    exists = db.query(Category).filter(Category.name == cat.name).first()
    if exists:
        raise HTTPException(status_code=400, detail="Category exists")
    c = Category(name=cat.name, description=cat.description or "")
    db.add(c); db.commit(); db.refresh(c)
    return c

@router.get("/categories", response_model=List[CategoryOut])
def list_categories(db: Session = Depends(get_db), admin=Depends(get_current_admin)):
    return db.query(Category).all()

@router.post("/challenges", response_model=ChallengeOut)
def add_challenge(ch: ChallengeCreate, db: Session = Depends(get_db), admin=Depends(get_current_admin)):
    cat = db.query(Category).get(ch.category_id)
    if not cat:
        raise HTTPException(status_code=404, detail="Category not found")
    c = Challenge(
        title=ch.title,
        description=ch.description,
        difficulty=ch.difficulty,
        points=ch.points,
        flag_hash=hash_flag(ch.flag),
        category_id=ch.category_id,
        storyline=ch.storyline,
        sequence=ch.sequence
    )
    db.add(c); db.commit(); db.refresh(c)
    return c

@router.get("/challenges", response_model=List[ChallengeOut])
def list_admin_challenges(db: Session = Depends(get_db), admin=Depends(get_current_admin)):
    return db.query(Challenge).all()
