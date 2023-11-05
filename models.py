from db import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

class Ticket(Base):
    __tablename__ = "tickets"
    tickets_id = Column(Integer, primary_key=True, index=True)
    tickets_name = Column(String, nullable=False)

class Question(Base):
    __tablename__ = 'questions'
    id = Column(Integer, primary_key=True, index=True)
    questions = Column(String)
    ticket_id = Column(Integer, ForeignKey("tickets.tickets_id"))


