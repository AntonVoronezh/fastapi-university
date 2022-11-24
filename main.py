# uvicorn main:app --reload
# uvicorn root-file-name:root-function-in-the-file --reload
from fastapi import FastAPI, status

from modules.students.controller import students_router
from modules.faculty.controller import faculties_router
from modules.student_info.controller import student_info_router

app = FastAPI()

for r in (
        students_router,
        faculties_router,
        student_info_router,
):
    app.include_router(r)

