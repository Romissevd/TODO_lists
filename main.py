from fastapi import FastAPI, Path

from schemas import Task, TaskOut

app = FastAPI()


@app.get('/')
def test():
    return {'key': 'Hello world'}


@app.post('/task/')
def create_task(item: Task):
    return TaskOut(**item.dict(), id=3)


@app.get('/task/{pk}/')
def get_single_task(pk: int = Path(..., gt=1)):
    return {'pk': pk}
