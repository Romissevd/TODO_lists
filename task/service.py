from datetime import datetime

from sqlalchemy.orm import Session

from task.models import Task
from task.schemas import TaskCreate
from user.models import User


def get_task_list(db: Session):
    return db.query(Task).all()


def create_user(db: Session, item: TaskCreate):
    # TODO add User to task
    user = db.query(User).get(1)
    task = Task(user=user.id, created_at=datetime.now(),  **item.dict())
    db.add(task)
    db.commit()
    db.refresh(task)
    return task
