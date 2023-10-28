from pydantic import BaseModel
from sqlalchemy import Column,Integer,String
from typing import ClassVar

class Tickets(BaseModel):
    __tablename__ = "tickets"
    id:ClassVar[int] = Column(Integer, primary_key=True)
    name:ClassVar[str] = Column(String)


class Questions(BaseModel):
    __tablename__ = "questions"
    id: ClassVar[int] = Column(Integer, primary_key=True)
    name: ClassVar[str] = Column(String)
    question:ClassVar[str] = Column(String)
