from database import Base
from sqlalchemy import Column, String, Date, UUID

class Contact(Base):
    __tablename__ = "contacts"
    id = Column(UUID, primary_key=True, index=True)
    name = Column(String)
    email = Column(String)
    message = Column(String)
    date = Column(Date)