from sqlalchemy import Column, Integer, ForeignKey
from db.base_class import Base


class ExamScore(Base):
    id = Column(Integer, primary_key=True)

    exam_id = Column(Integer, ForeignKey("exam.id"))
    score_id = Column(Integer, ForeignKey("score.id"))
