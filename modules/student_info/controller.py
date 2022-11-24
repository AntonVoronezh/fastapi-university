from db.db import db
from models.student_info import StudentInfoDTO
from shared.controllers import api_router_factory
from tables.generate_tables import StudentInfo

student_info_router = api_router_factory("student_info")


@student_info_router.get('/', response_model=list[StudentInfoDTO], status_code=200,
                     name='Получение информации по всем студентам')
def get_all_student_info():
    student_infos = db.query(StudentInfo).all()
    return student_infos


@student_info_router.get('/{id}', response_model=StudentInfoDTO, status_code=200, name='Получение информации по одному студенту')
def get_student_info(id: int):
    student_info = db.query(StudentInfo).filter(StudentInfo.id == id).first()

    return student_info


@student_info_router.put('/{id}', response_model=StudentInfoDTO, status_code=200, name='Обновление информации по одному студенту')
def update_student_info(id: int, item: StudentInfoDTO):
    student_info_to_update = db.query(StudentInfo).filter(StudentInfo.id == id).first()

    student_info_to_update.age = item.age
    student_info_to_update.address = item.address

    db.commit()

    return student_info_to_update
