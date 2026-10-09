from pydantic import BaseModel
from datetime import date

class ContactCreate(BaseModel):
    name: str
    email: str
    message: str
    date: date