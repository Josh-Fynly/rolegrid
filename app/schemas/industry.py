from pydantic import BaseModel


class IndustryCreate(BaseModel):
    name: str


class IndustryUpdate(BaseModel):
    name: str


class IndustryResponse(BaseModel):
    id: int
    name: str

    class Config:
        from_attributes = True
