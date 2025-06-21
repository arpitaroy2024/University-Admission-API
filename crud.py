from sqlalchemy.orm import Session
import models, schemas

def create_applicant(db: Session, applicant: schemas.ApplicantInformationCreate):
    new_applicant = models.ApplicantInformation(**applicant.dict())
    db.add(new_applicant)
    db.commit()
    db.refresh(new_applicant)
    return new_applicant

def get_applicants(db: Session):
    return db.query(models.ApplicantInformation).all()

def create_ssc_marksheet(db: Session, marksheet: schemas.SSCMarksheetCreate):
    new_marksheet = models.SSCMarksheet(**marksheet.dict())
    db.add(new_marksheet)
    db.commit()
    db.refresh(new_marksheet)
    return new_marksheet

def create_hsc_marksheet(db: Session, marksheet: schemas.HSCMarksheetCreate):
    new_marksheet = models.HSCMarksheet(**marksheet.dict())
    db.add(new_marksheet)
    db.commit()
    db.refresh(new_marksheet)
    return new_marksheet
