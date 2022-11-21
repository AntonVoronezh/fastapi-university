# uvicorn main:app --reload
from fastapi import FastAPI
from pydantic import BaseModel

from db.db import SessionLocal
from models.student import StudentDTO
from utils.generate_student import Student

app = FastAPI()
db = SessionLocal()

#
# for it in db.query(Student):
#     print(it.name)

@app.get('/students', response_model=list[StudentDTO], status_code=200, name='Получение всех записей')
# @app.get('/students',  status_code=200, name='Получение всех записей')
def get_all_items():
    items = db.query(Student).all()
    return items
