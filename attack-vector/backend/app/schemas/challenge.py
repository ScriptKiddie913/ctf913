from pydantic import BaseModel
from typing import Optional

class CategoryOut(BaseModel):
    id: int
    name: str
    description: str
    class Config:
        from_attributes = True

class ChallengeCreate(BaseModel):
    title: str
    description: str
    difficulty: str
    points: int
    flag: str
    category_id: int
    storyline: Optional[str] = None
    sequence: Optional[int] = None

class ChallengeOut(BaseModel):
    id: int
    title: str
    description: str
    difficulty: str
    points: int
    category_id: int
    storyline: Optional[str] = None
    sequence: Optional[int] = None
    class Config:
        from_attributes = True
