from fastapi import APIRouter,Depends,HTTPException
from db import get_db,engine,Base,create_engine
from models import Question,Ticket
from sqlalchemy.orm import Session
from schemas import Question_create
import random
Base.metadata.create_all(engine)

router = APIRouter()

@router.get("/questions/")
async def get_questions(db=Depends(get_db)):
    chec = db.query(Question).all
    return chec


@router.get("/questions/random/{ticket_id}/")
async def get_random_question(ticket_id: int, db = Depends(get_db)):
    check = db.query(Question).filter(Question.ticket_id == ticket_id).all()
    if not check:
        raise HTTPException(status_code=404, detail="No questions found for this ticket.")
    else:
        random_question = random.choice(check)
        return {"question_text": random_question.questions}


@router.post("/add/questions/to/ticket")
def create_question(question:Question_create, db = Depends(get_db)):
    chec = db.query(Ticket).filter(Ticket.tickets_id == question.ticket_id).first()

    if not chec:
        raise HTTPException(status_code=404, detail=" not found")

    db_comment = Question()
    db_comment.ticket_id= question.ticket_id
    db_comment.questions = question.question
    db.add(db_comment)
    db.commit()
    db.refresh(db_comment)

    return db_comment

@router.delete("/tickets/{ticket_id}/questions/")
def delete_questions(ticket_id: int, db: Session = Depends(get_db)):
    deleted_count = db.query(Question).filter(Question.ticket_id == ticket_id).first()
    if not deleted_count:
        raise HTTPException(status_code=404, detail="No questions found for this ticket")
    db.delete(deleted_count)
    db.commit()
    return {"message": f"Deleted {deleted_count} questions"}