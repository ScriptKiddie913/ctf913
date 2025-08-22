from pydantic import BaseModel

class SubmitFlagRequest(BaseModel):
    challenge_id: int
    flag: str

class SubmissionOut(BaseModel):
    id: int
    challenge_id: int
    correct: bool
    class Config:
        from_attributes = True
