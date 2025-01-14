from pydantic import BaseModel, EmailStr
from datetime import datetime

class UserBase(BaseModel):
    name: str
    email: EmailStr

class UserCreate(UserBase):
    pass

class UserResponse(UserBase):
    id: int

    class Config:
        orm_mode = True

class AuditLogResponse(BaseModel):
    id: int
    action: str
    details: str
    timestamp: datetime

    class Config:
        orm_mode = True

