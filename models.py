from db import Base,engine
from sqlalchemy import Column, Integer, String,ForeignKey
from sqlalchemy.orm import relationship
Base.metadata.create_all(engine)

class Ticket(Base):
    __tablename__ = "tickets"
    tickets_id = Column(Integer, primary_key=True, index=True)
    tickets_name = Column(String, nullable=False)
class Question(Base):
    __tablename__ = 'questions'
    questions_id = Column(Integer, primary_key=True, index=True)
    questions_name = Column(String, nullable=False)
    ticket_id = Column(Integer, ForeignKey('tickets.tickets_id'))
    ticket_rel = relationship(Ticket, backref='tickets')



