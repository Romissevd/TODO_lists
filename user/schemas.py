from datetime import datetime

from pydantic import BaseModel, Field


class UserBase(BaseModel):
    first_name: str = Field(..., max_length=25)
    last_name: str = Field(..., max_length=50)
    username: str = Field(..., max_length=25)

    class Config:
        orm_mode = True


class UserList(UserBase):
    id: int


class UserCreate(UserBase):
    password: str


class UserTask(UserBase):
    id: int
    first_name: str
    last_name: str
