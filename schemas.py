from pydantic import BaseModel, EmailStr

class ApplicantInformationBase(BaseModel):
    applicant_id : int
    Exam_Roll : int
    name :str
    father_name :str
    mother_name : str
    exam_unit : str
    exam_question_type :str

class ApplicantInformationCreate(ApplicantInformationBase):
    pass

class ApplicantInformationResponse(ApplicantInformationBase):
    Candidate_ID: int

    class Config:
        from_attributes = True

class SSCMarksheetBase(BaseModel):
    Exam_Roll: int
    SSC_GPA: str

class HSCMarksheetBase(BaseModel):
    Exam_Roll: int
    HSC_GPA: str

class SSCMarksheetCreate(SSCMarksheetBase):
    pass

class HSCMarksheetCreate(HSCMarksheetBase):
    pass

class SSCMarksheetResponse(SSCMarksheetBase):
    ID: int

    class Config:
        from_attributes = True

class HSCMarksheetResponse(HSCMarksheetBase):
    ID: int

    class Config:
        from_attributes = True
