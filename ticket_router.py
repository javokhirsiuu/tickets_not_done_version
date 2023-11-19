from fastapi import Depends, HTTPException, APIRouter
from sqlalchemy.orm import Session
from db import get_db
from models import Ticket
from schemas import Ticket_create,ticket_update
import random

router = APIRouter()

@router.get("/tickets/")
async def get_tickets(db=Depends(get_db)):
    users = db.query(Ticket).all()
    return users
@router.post("/tickets/")
async def create_ticket(ticket: Ticket_create,db = Depends(get_db)):
    check = db.query(Ticket).filter(Ticket.tickets_name == ticket.name).first()
    if check is not None:
        raise HTTPException(status_code=404,detail='already exists')

    db_modul = Ticket()
    db_modul.tickets_name = ticket.name
    # db.refresh(db_modul)
    db.add(db_modul)
    db.commit()
    return db



@router.get("/{ticket_id}")
async def get_ticket(id: int, db=Depends(get_db)):
    user = db.query(Ticket).filter(Ticket.tickets_id == id).first()
    if not user:
        raise HTTPException(status_code=404, detail=" not found")
    return user

@router.put("/edit/ticket")
async def edit(ticket_id:int,ticket_new:str,db=Depends(get_db)):
    db_ticket = db.query(Ticket).filter(Ticket.tickets_id == ticket_id).first()
    if not db_ticket:
        raise HTTPException(status_code=404, detail="Ticket not found")
    else:
        db_ticket.tickets_name=ticket_new
        db.commit()
        db.refresh(db_ticket)
        return db_ticket


@router.delete("/tickets/{ticket_id}/")
async def delete_ticket(ticket_id: int,db=Depends(get_db)):
    chunk = db.query(Ticket).filter(Ticket.tickets_id==ticket_id).first()
    if not chunk:
        raise HTTPException(status_code=404,detail="not found")
    else:
        db.delete(chunk)
        db.commit()
        return {"message": f"Ticket {ticket_id} deleted"}
