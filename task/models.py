from sqlalchemy import Column, String, Text, Integer, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from core.db import Base
from user.models import User


class Task(Base):
    __tablename__ = 'tasks'
    id = Column(Integer, primary_key=True, index=True, unique=True)
    title = Column(String)
    description = Column(Text)
    created_at = Column(DateTime)
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship(User)
