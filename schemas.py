from datetime import datetime

from pydantic import BaseModel, Field


class User(BaseModel):
    first_name: str = Field(..., max_length=25)
    last_name: str = Field(..., max_length=50)


class Task(BaseModel):
    title: str = Field(..., max_length=100)
    description: str = None
    author: User
    created_at: datetime


class TaskOut(Task):
    id: int
