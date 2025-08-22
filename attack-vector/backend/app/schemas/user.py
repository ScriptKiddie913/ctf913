from pydantic import BaseModel, EmailStr

class UserOut(BaseModel):
    id: int
    email: EmailStr
    is_admin: bool
    class Config:
        from_attributes = True
