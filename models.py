from database import Base
from sqlalchemy import Column, String, Date

class Contact(Base):
    name = Column(String)
    email = Column(String)
    message = Column(String)
    date = Column(Date)