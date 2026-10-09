import models
import schemas
from database import get_db, engine

from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from fastapi.responses import JSONResponse

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.post('/contact/')
def create_contact(data: schemas.ContactCreate, db: Session = Depends(get_db)):
    data = models.Contact(**data.model_dump())
    db.add(data)
    db.commit()
    db.refresh(data)
    return JSONResponse(status_code=201, content={"message":"saved"})
