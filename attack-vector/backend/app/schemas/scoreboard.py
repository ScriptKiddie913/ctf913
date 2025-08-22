from pydantic import BaseModel

class ScoreboardEntry(BaseModel):
    user_id: int
    email: str
    score: int
