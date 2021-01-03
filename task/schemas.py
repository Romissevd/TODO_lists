from datetime import datetime

from pydantic import BaseModel, Field
from user.schemas import UserBase


class Task(BaseModel):
    title: str = Field(..., max_length=100)
    description: str = None
    author: UserBase
    created_at: datetime


class TaskOut(Task):
    id: int
