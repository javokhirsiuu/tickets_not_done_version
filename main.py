from fastapi import FastAPI
from tickets import router as tickets
app = FastAPI()

app.include_router(tickets)
Base.metadata.create_all(engine)
