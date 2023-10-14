from pydantic import BaseModel
from sqlalchemy import Column,Integer,String

class Tickets(BaseModel):
    __tablename__ = "tickets"
    class Config:
        ignored_types = type[int]
    id = Column(Integer,primary_key=True,nullable=False)
    name = Column(String,nullable=False)

class Questions(BaseModel):
    id = Column(Integer,primary_key=True,nullable=False)
    question = Column(String,nullable=False)
    name = Column(String,nullable=False)