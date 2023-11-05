from fastapi import FastAPI
from db import Base, engine
from question_router import router as question_router
from ticket_router import router as ticket_router
Base.metadata.create_all(engine, checkfirst=True)

app = FastAPI()

app.include_router(question_router)
app.include_router(ticket_router)
