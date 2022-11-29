from pydantic import BaseModel


class HousingBaseDto(BaseModel):
    name: str
    faculty_id: int or None


class HousingDTO(HousingBaseDto):
    id: int

    class Config:
        orm_mode = True
