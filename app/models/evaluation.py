from sqlalchemy import Column, Integer, Text, ForeignKey, Float
from sqlalchemy.orm import relationship

from app.core.database import Base


class Evaluation(Base):
    __tablename__ = "evaluations"

    id = Column(Integer, primary_key=True, index=True)

    submission_id = Column(Integer, ForeignKey("submissions.id"))
    score = Column(Float, default=0.0)
    feedback = Column(Text)

    submission = relationship("Submission")
