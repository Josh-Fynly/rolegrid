from pydantic import BaseModel


class RoleCreate(BaseModel):
    name: str
    industry_id: int


class RoleUpdate(BaseModel):
    name: str
    industry_id: int


class RoleResponse(BaseModel):
    id: int
    name: str
    industry_id: int

    class Config:
        from_attributes = True
