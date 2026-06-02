from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from app.core.database import Base


class Role(Base):
    __tablename__ = "roles"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)

    industry_id = Column(Integer, ForeignKey("industries.id"))

    industry = relationship("Industry")
