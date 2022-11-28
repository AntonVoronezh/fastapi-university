from models.faculty import FacultyBaseDto
from models.housing import HousingDTO
from models.student import StudentDTO


class FacultyBaseWithStudentsDto(FacultyBaseDto):
    name: str
    students: list[StudentDTO] = []
    housing: list[HousingDTO] = []


class FacultyWithStudentsDTO(FacultyBaseWithStudentsDto):
    id: int

    class Config:
        orm_mode = True
