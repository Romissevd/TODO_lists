from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from core.utils import get_db
from task import schemas, service


router = APIRouter()


@router.get('/', response_model=List[schemas.TaskOut])
def tasks(db: Session = Depends(get_db)):
    list_tasks = service.get_task_list(db)
    return list_tasks


@router.post('/', response_model=schemas.TaskOut)
def task(item: schemas.TaskCreate, db: Session = Depends(get_db)):
    new_task = service.create_user(db, item=item)
    return new_task


# @router.get('/{pk}/')
# def get_single_task(pk: int = Path(..., gt=1)):
#     return {'pk': pk}

# @router.get('/search_task/')
# def search_tasks(search: str = Query(..., description='Search tasks')):
#     return search