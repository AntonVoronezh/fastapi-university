# uvicorn main:app --reload
# uvicorn root-file-name:root-function-in-the-file --reload
from fastapi import FastAPI, status

from modules.students.controller import students_router

app = FastAPI()

for r in (
        students_router,
):
    app.include_router(r)

