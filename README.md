# TODO_lists
### Technology
* Python 3.8
* Fast API
* Uvicorn


Run project
```
uvicorn main:app --port 8001
```

Commands
* create migrations
```
alembic revision --autogenerate -m "message"
```
* migrate
```
alembic upgrade head
```
