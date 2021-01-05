from datetime import datetime

from pydantic import BaseModel, Field
from user.schemas import UserTask


class Task(BaseModel):
    title: str = Field(..., max_length=100)
    description: str = None

    class Config:
        orm_mode = True


class TaskOut(Task):
    id: int
    user: UserTask
    created_at: datetime


class TaskCreate(Task):
    pass