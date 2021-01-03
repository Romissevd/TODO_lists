from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from core.utils import get_db
from task import schemas


router = APIRouter()


@router.get('/')
def test(db: Session = Depends(get_db)):
    return {'key': 'Hello world'}


# @router.post('/', response_model=TaskOut, response_model_exclude_unset=False)
# def create_task(item: Task):
#     return TaskOut(**item.dict(), id=3)
#
#
# @router.get('/{pk}/')
# def get_single_task(pk: int = Path(..., gt=1)):
#     return {'pk': pk}
#
#
# @router.get('/search_task/')
# def search_tasks(search: str = Query(..., description='Search tasks')):
#     return search