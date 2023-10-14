from fastapi import APIRouter,Depends
import random
from sqlalchemy.orm import Session
from ticket_modul import Tickets,Questions
from schemas import Ticketss,question
from db import get_db
router = APIRouter()


num_questions_per_ticket = 20
num_tickets = 50
@router.get("/get_ticket/{ticket_number}")
async def get_ticket(ticket_number: int):
    if ticket_number < 1 or ticket_number > num_tickets:
        return {"error": "Билет с таким номером не существует"}


@router.post("add/ticket/")
async def create_ticket(ticket:Tickets,db:Session=Depends(get_db)):
   db_modul = Ticketss
   db_modul.id = ticket.id
   db_modul.name = ticket.name
   db.add(db_modul)
   db.commit()
   return f"{db_modul}added"

@router.post("add/question")
async def add(question:question,db:Depends(get_db)):
    db_modul = question
    db_modul.name = question.name
    db_modul.id = question.id
    db_modul.question = question.question
    db.add(db_modul)
    db.commit()
    return db_modul

