from pydantic import BaseModel
from sqlalchemy import Column,Integer,String

class Tickets(BaseModel):
    __tablename__ = "tickets"
    id = Column(Integer,primary_key=True,index=True)
    name = Column(String,nullable=False)

class Questions(BaseModel):
    __tablename__ = "questions"
    id = Column(Integer,primary_key=True,index=True)
    question = Column(String,nullable=False)
    name = Column(String,nullable=False)
