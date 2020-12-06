from sqlalchemy import Column, String, DateTime, Integer, Boolean

from core.db import Base


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, unique=True, index=True)
    username = Column(String(25), unique=True)
    password = Column(String)
    last_name = Column(String(length=25))
    first_name = Column(String(length=25))
    created_at = Column(DateTime)
    is_active = Column(Boolean, default=False)
    is_admin = Column(Boolean, default=False)