# uvicorn main:app --reload
# uvicorn root-file-name:root-function-in-the-file --reload
from fastapi import FastAPI, status

from modules.faculty.controller import faculties_router
from modules.housing.controller import housing_router
from modules.group.controller import group_router
from modules.subject.controller import subjects_router

app = FastAPI()




for r in (
        faculties_router,
        housing_router,
        group_router,
        subjects_router,
):
    app.include_router(r)
