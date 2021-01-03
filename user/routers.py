from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from core.utils import get_db
from user import service, schemas


router = APIRouter()


@router.get('/', response_model=List[schemas.UserList])
def task_list(db: Session = Depends(get_db)):
    users = service.get_user_list(db)
    return users


@router.post('/')
def task_list(item: schemas.UserCreate, db: Session = Depends(get_db)):
    user = service.create_user(db, item=item)
    return user
