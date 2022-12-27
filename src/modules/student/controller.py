from fastapi import Depends

from src.modules.student.dto import StudentDTO
from src.modules.student.service import StudentService
from src.shared.controllers import api_router_factory

student_router = api_router_factory("student")


@student_router.get('/',
                    # response_model=list[StudentDTO],
                    summary='Получение всех студентов')
async def get_all(student_service: StudentService = Depends(StudentService)):
    return await student_service.all()


@student_router.get('/{id}', status_code=200, summary='Получение студента')
async def get_by_id(id: int, service: StudentService = Depends(StudentService)):
    return await service.get(id)

#
# @student_router.post('/', response_model=StudentBaseDto, status_code=201, name='Запись нового студента')
# def update_student(item: StudentBaseDto = Body(),
#                    student_service: StudentService = Depends(get_student_service)):
#     new_student = {'first_name': item.first_name, 'second_name': item.second_name,
#                    'family': item.family, 'age': item.age, 'group_id': item.group_id,
#                    # 'info': dict(description='description', img='img', student_id=1, address='address')
#                    }
#
#     return student_service.create(new_student)


# def create_student(item: StudentBaseDto = Body()) -> StudentDTO:
#     new_student = Student(first_name=item.first_name, second_name=item.second_name,
#                           family=item.family, age=item.age, group_id=item.group_id)
#     new_student.info = StudentInfo(description='description', img='img', student_id=1, address='address')
#
#     db.add(new_student)
#     db.commit()
#
#     return new_student

#
# @student_router.put('/{id}', response_model=StudentDTO, status_code=200, name='Обновление студента')
# def update_student(id: int, item: StudentBaseUpdateDto = Body()) -> StudentDTO:
#     student_to_update = db.query(Student).filter(Student.id == id).first()
#
#     student_to_update.first_name = item.first_name
#     student_to_update.second_name = item.second_name
#     student_to_update.family = item.family
#     student_to_update.age = item.age
#     student_to_update.group_id = item.group_id
#
#     db.commit()
#     return student_to_update
#
#
# @student_router.delete('/{id}', status_code=204, name='Удаление студента')
# def delete_student(id: int) -> StudentDTO:
#     student_to_delete = db.query(Student).filter(Student.id == id).first()
#
#     if student_to_delete is None:
#         raise HTTPException(status_code=404, detail='факультет не найден')
#
#     db.delete(student_to_delete)
#     db.commit()
#     db.close()
#     return student_to_delete
