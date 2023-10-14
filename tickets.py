from fastapi import APIRouter,Depends,H
import random
from sqlalchemy.orm import Session
from ticket_modul import Tickets,Questions
from schemas import Ticketss,question
from db import get_db
router = APIRouter()


num_questions_per_ticket = 20
num_tickets = 50
@router.get("/get_ticket/{ticket_number}")
async def get_ticket(ticket_number: int,db:Session=Depends(get_db)):
    db = db.query(Tickets).filter(Tickets.id ==ticket_number)
    if not db:
        return {"error": "Билет с таким номером не существует"}
    else:
        return { ticket_number: Questions}


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

@router.put("change/ticket")
async def update_ticket(updated_name:Updated_ticket,db:Session = Depends(get_db)):
    db = db.query(Tickets).filter(Tickets.name==updated_name).first()
    if not db:
        raise HTTPException(status_code = 404,detail ="not exists")
    else:
        db_modul = Ticketss
        db_modul.name = updated_name.updated_name
        db.add(db_modul)
        db.refresh()
        db.commit()
        return db_modul
@router.put("change/ticket")
async def update_questio(updated_name:Updated_ticket,db:Session = Depends(get_db)):
    db = db.query(Tickets).filter(Tickets.name==updated_name).first()
    if not db:
        raise HTTPException(status_code = 404,detail ="not exists")
    else:
        db_modul = Ticketss
        db_modul.name = updated_name.updated_name
        db.add(db_modul)
        db.refresh()
        db.commit()
        return db_modul

@router.put("change/ticket")
async def update_ticket(updated_data:updated_question,db:Session = Depends(get_db)):
    db = db.query(Tickets).filter(Tickets.name==updated_data).first()
    if not db:
        raise HTTPException(status_code = 404,detail ="not exists")
    else:
        db_modul = Questions
        db_modul.name = updated_data.updated_name
        db_modul.question = updated_data.question
        db.add(db_modul)
        db.refresh()
        db.commit()
        return db_modul


@router.delete("api/delete")
async def delete_(id:int,question:question,ticket:Ticketss,db:Session=Depends(get_db)):
    db = db.query(Tickets).filter(Tickets.id ==id).first()
    if not db:
        raise HTTPException(status_code =404,detail="not found")
    else:
        db_modul = Tickets
        db_modul1 = Questions
        db_modul.id = id
        db_modul.name = ticket.name
        db_modul1.question = question.question
        db.delete(db_modul)
        db.delete(db_modul1)
        return "deleted"



        

