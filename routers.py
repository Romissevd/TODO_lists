from fastapi import APIRouter

import user.routers
import task.routers


router = APIRouter()

router.include_router(user.routers.router, prefix='/users')
router.include_router(task.routers.router, prefix='/tasks')
