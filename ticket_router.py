from fastapi import Depends, HTTPException, APIRouter
from sqlalchemy.orm import Session
from db import get_db
from models import Ticket
from schemas import Ticket_create
import random
from config import AUTH_USE_REQUEST_HEADERS
router = APIRouter()

AUTH_USE_REQUEST_HEADERS
@router.get("/tickets/")
async def get_tickets(db=Depends(get_db)):
    users = db.query(Ticket).all()
    return users
@router.post("/tickets/")
async def create_ticket(ticket: Ticket_create,db: Session = Depends(get_db)):
    check = db.query(Ticket).filter(Ticket.tickets_name == ticket.name).first()
    if check is not None:
        raise HTTPException(status_code=404,
                            detail='already exists')


    db_modul = Ticket()
    db_modul.tickets_name = ticket.name
    db.add(db_modul)
    db.commit()
    db.refresh(db_modul )
    return db

@router.get("/question")
async def get_question(id:int,db = Depends(get_db)):
    check = db.query(Ticket).filter(Ticket.tickets_id==id).first()
    if not check:
        raise HTTPException(status_code=404,detail="does not exist")
    else:

        return {random.choice(check)}

@router.get("/{ticket_id}")
async def get_ticket(id: int, db=Depends(get_db)):
    user = db.query(Ticket).filter(Ticket.tickets_id == id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user
@router.put("/edit-ticket")
async def ticket_edit(id,schema:str ,db = Depends(get_db)):

    model = db.query(Ticket).filter(Ticket.tickets_id == id).first()
    if model is None:
        raise HTTPException(status_code=404, detail="not found")
    else:
        model.name = schema
        db.add(model)
        db.commit()
        db.refresh(model)
        return model



@router.delete("/tickets/{ticket_id}/")
async def delete_ticket(ticket_id: int,db=Depends(get_db)):
    chunk = db.query(Ticket).filter(Ticket.tickets_id==ticket_id).first()
    if not chunk:
        raise HTTPException(status_code=404,detail="not found")
    else:
        db.delete(chunk)
        db.commit()
        return {"message": f"Ticket {ticket_id} deleted"}