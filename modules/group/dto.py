from pydantic import BaseModel


class GroupBaseDto(BaseModel):
    name: str


class GroupDTO(GroupBaseDto):
    id: int

    class Config:
        orm_mode = True


