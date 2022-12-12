# uvicorn main:app --reload
# uvicorn root-file-name:root-function-in-the-file --reload

# https://www.compose.com/articles/schema-migrations-with-alembic-python-and-postgresql/
# alembic init alembic
# alembic
# alembic revision -m "baseline"  - создание базовый сценарий для текущего состояния базы данных
# alembic upgrade head - команда гарантирует, что база данных обновлена ​​до самой последней версии
# alembic revision --autogenerate -m "add aaaaaaa table" - добавить после изменения
# alembic upgrade head - применить изменения
# alembic current - текущие изменения
# alembic downgrade -1 - отменить изменеия



from fastapi import FastAPI, status

from modules.faculty.controller import faculties_router
from modules.housing.controller import housing_router
from modules.group.controller import group_router
from modules.subject.controller import subjects_router
from modules.student.controller import student_router

app = FastAPI()

for r in (
        # student_router,
        # faculties_router,
        housing_router,
        group_router,
        subjects_router,
):
    app.include_router(r)
