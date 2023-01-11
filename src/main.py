# uvicorn src.main:app --reload
# uvicorn root-file-name:root-function-in-the-file --reload

from fastapi import Depends, FastAPI

from src.db.db import User
from src.modules.student.controller import student_router
from src.modules.user.dto import UserRead, UserCreate, UserUpdate
from src.modules.user.service import fastapi_users, auth_backend, current_active_user

# https://fastapi-users.github.io/
# https://harrisonmorgan.dev/2021/02/15/getting-started-with-fastapi-users-and-alembic/
# https://www.compose.com/articles/schema-migrations-with-alembic-python-and-postgresql/
# alembic init src/alembic
# alembic
# alembic revision -m "baseline"  - создание базовый сценарий для текущего состояния базы данных
# alembic upgrade head - команда гарантирует, что база данных обновлена ​​до самой последней версии
# alembic revision --autogenerate -m "add aaaaaaa table" - добавить после изменения
# alembic upgrade head - применить изменения
# alembic current - текущие изменения
# alembic downgrade -1 - отменить изменеия

app = FastAPI()

for r in (
        student_router,
):
    app.include_router(r)

app.include_router(
    fastapi_users.get_auth_router(auth_backend), prefix="/auth/jwt", tags=["auth"]
)
app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["auth"],
)
app.include_router(
    fastapi_users.get_reset_password_router(),
    prefix="/auth",
    tags=["auth"],
)
app.include_router(
    fastapi_users.get_verify_router(UserRead),
    prefix="/auth",
    tags=["auth"],
)
app.include_router(
    fastapi_users.get_users_router(UserRead, UserUpdate),
    prefix="/users",
    tags=["users"],
)


@app.get("/authenticated-route")
async def authenticated_route(user: User = Depends(current_active_user)):
    return {"message": f"Hello {user.email}!"}
