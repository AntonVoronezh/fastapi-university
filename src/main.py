# uvicorn src.main:app --reload
# uvicorn root-file-name:root-function-in-the-file --reload
import os

from dotenv import load_dotenv
from fastapi import FastAPI

from src.db.config import get_settings
from src.modules.student.controller import student_router


# https://www.compose.com/articles/schema-migrations-with-alembic-python-and-postgresql/
# alembic init src/alembic
# alembic
# alembic revision -m "baseline"  - создание базовый сценарий для текущего состояния базы данных
# alembic upgrade head - команда гарантирует, что база данных обновлена ​​до самой последней версии
# alembic revision --autogenerate -m "add aaaaaaa table" - добавить после изменения
# alembic upgrade head - применить изменения
# alembic current - текущие изменения
# alembic downgrade -1 - отменить изменеия


# BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# load_dotenv(os.path.join(BASE_DIR, ".env"))
# database_url = os.environ["DATABASE_URL"]

# fff = get_settings().database_url

app = FastAPI()

# @app.get('/')
# def gggg():
#     return {'fff': fff}

for r in (
        student_router,
):
    app.include_router(r)
