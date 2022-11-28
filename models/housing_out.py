from models.faculty import FacultyDTO
from models.housing import HousingBaseDto


class HousingBaseWithFacultyDto(HousingBaseDto):
    name: str
    faculty: list[FacultyDTO] = []


class HousingWithFacultyDTO(HousingBaseWithFacultyDto):
    id: int

    class Config:
        orm_mode = True
