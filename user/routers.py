from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from core.utils import get_db
from user import service, schemas


router = APIRouter()


@router.get('/', response_model=List[schemas.UserList])
def users(db: Session = Depends(get_db)):
    users_list = service.get_user_list(db)
    return users_list


@router.post('/')
def user(item: schemas.UserCreate, db: Session = Depends(get_db)):
    new_user = service.create_user(db, item=item)
    return new_user
