from pydantic import BaseModel


class Ticket_create(BaseModel):
    name: str




class Question_create(BaseModel):
    question:str
    ticket_id:int

class Ticket_schema(BaseModel):
    id: int
    name: str



class Question_schema(BaseModel):
    question: str


class ticket_update(BaseModel):
    new_name:str
    id:int

class Ticket_read(BaseModel):
    ticket_name:str
    questions:str