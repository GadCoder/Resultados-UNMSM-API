from sqlalchemy import Column, Integer, ForeignKey
from db.base_class import Base


class MajorScore(Base):
    id = Column(Integer, primary_key=True)

    major_id = Column(Integer, ForeignKey("major.id"), nullable=False)
    exam_id = Column(Integer, ForeignKey("exam.id"), nullable=False)
    score_id = Column(Integer, ForeignKey("score.id"), nullable=False)
