# uvicorn main:app --reload
from fastapi import FastAPI

from db import db
from models.student import Student

app = FastAPI()


# @app.get('/items', status_code=200, name='Получение всех записей')
@app.get('/items', response_model=list[Student], status_code=200, name='Получение всех записей')
def get_all_items():
    items = db.query(Student).all()
    return items


