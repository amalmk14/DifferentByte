from pydantic import BaseModel
from datetime import timezone

class ContactCreate(BaseModel):
    name: str
    email: str
    message: str
    date: str