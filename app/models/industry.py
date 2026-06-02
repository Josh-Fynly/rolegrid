from sqlalchemy import Column, Integer, String
from app.core.database import Base


class Industry(Base):
    __tablename__ = "industries"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, nullable=False)
