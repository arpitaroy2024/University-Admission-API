from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
import models, schemas, crud
from database import engine, SessionLocal

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependency = Depends(get_db)

@app.post("/applicants/", response_model=schemas.ApplicantInformationResponse)
def create_applicant(applicant: schemas.ApplicantInformationCreate, db: Session = db_dependency):
    return crud.create_applicant(db, applicant)

@app.get("/applicants/")
def get_applicants(db: Session = db_dependency):
    return crud.get_applicants(db)

@app.post("/ssc_marksheet/", response_model=schemas.SSCMarksheetResponse)
def create_ssc_marksheet(marksheet: schemas.SSCMarksheetCreate, db: Session = db_dependency):
    return crud.create_ssc_marksheet(db, marksheet)

@app.post("/hsc_marksheet/", response_model=schemas.HSCMarksheetResponse)
def create_hsc_marksheet(marksheet: schemas.HSCMarksheetCreate, db: Session = db_dependency):
    return crud.create_hsc_marksheet(db, marksheet)


