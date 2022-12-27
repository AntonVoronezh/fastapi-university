from fastapi import Depends, Body
from starlette import status

from src.modules.student.dto import StudentCreateDTO
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


@student_router.post(
    "/",
    # response_model=StudentDTO,
    summary="Создание студента",
)
async def create(
        data: StudentCreateDTO = Body(),
        service: StudentService = Depends(StudentService),
):
    return await service.create(item=data)


@student_router.put(
    "/{id}",
    # response_model=StudentDTO,
    summary="Обновление студента",
)
async def update(
        id: int,
        item: StudentCreateDTO,
        service: StudentService = Depends(StudentService),
):
    return await service.update(id, item=item)


@student_router.delete(
    "/{id}",
    status_code=status.HTTP_200_OK,
)
async def delete(
        id: int, service: StudentService = Depends(StudentService)
):
    await service.delete(id)
    return {"detail": "deleted"}
