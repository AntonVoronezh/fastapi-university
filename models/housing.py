from pydantic import BaseModel

class HousingBaseDto(BaseModel):
    name: str


class HousingDTO(HousingBaseDto):
    id: int

    class Config:
        orm_mode = True
