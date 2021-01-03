from sqlalchemy.orm import Session

from user.models import User
from user.schemas import UserCreate


def get_user_list(db: Session):
    return db.query(User).all()


def create_user(db: Session, item: UserCreate):
    user = User(**item.dict())
    db.add(user)
    db.commit()
    db.refresh(user)
    return user
