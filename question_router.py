from fastapi import APIRouter, Depends, HTTPException
from db import get_db, engine, Base
from models import Question
import random
Base.metadata.create_all(engine)

router = APIRouter()


@router.get("/all/question")
async def all_question(db=Depends(get_db)):
    query1 = db.query(Question).all()
    return query1


@router.get("/question/{id}")
async def get_question(id: int, db=Depends(get_db)):
    query = db.query(Question).filter(Question.questions_id == id).first()

    if not query:
        raise HTTPException(status_code=404, detail="tupoymisan")

    return query


@router.post("/add")
async def create(question: str, db=Depends(get_db)):
    model = Question()
    model.questions_name = question
    db.add(model)
    db.commit()
    return model
@router.get("/random/question")
async def get_random(db=Depends(get_db)):
    ticket = db.query(Question).all()
    if not ticket:
        raise HTTPException(status_code=404, detail="No")

    random_ticket = random.choice(ticket)

    return random_ticket


@router.put("/edit/question/")
async def edit(id: int, update: str, db=Depends(get_db)):
    updater = db.query(Question).filter(Question.questions_id == id).first()
    if not updater:
        raise HTTPException(status_code=404, detail="try again")

    else:
        updater.questions_name = update
        db.add(updater)
        db.commit()
        db.refresh(updater)
        return updater


@router.delete("/delete")
async def delete_com(ID: int, db=Depends(get_db)):
    comment = db.query(Question).filter(Question.questions_id == ID).first()
    if not comment:
        raise HTTPException(status_code=404, detail="comment not found")
    db.delete(comment)
    db.refresh(comment)
    return "comment deleted successfully"
