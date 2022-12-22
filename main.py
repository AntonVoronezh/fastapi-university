# uvicorn main:app --reload
# uvicorn root-file-name:root-function-in-the-file --reload
from fastapi import FastAPI

from modules.student.controller import student_router


# https://www.compose.com/articles/schema-migrations-with-alembic-python-and-postgresql/
# alembic init alembic
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
