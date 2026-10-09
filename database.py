import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

load_dotenv()

# BASE_URL = os.getenv("DATABASE_URL")
BASE_URL = "postgresql://postgres:Amal1234@localhost:5432/DifferentByte"

engine = create_engine(BASE_URL)
sessionLocal = sessionmaker(autoflush=False, autocommit=False, bind=engine)
Base = declarative_base()

def get_db():
    db = sessionLocal()
    try:
        yield db
    finally:
        db.close()