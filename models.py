from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class ApplicantInformation(Base):
    __tablename__ = "applicant_information"

    applicant_id = Column(Integer, primary_key=True, index=True)
    Exam_Roll = Column(Integer, unique=True, nullable=False)
    name = Column(String(100), nullable=False)
    father_name = Column(String(100), nullable=False)
    mother_name = Column(String(100), nullable=False)
    exam_unit = Column(String(10), nullable=False)
    exam_question_type = Column(String(20), nullable=False)

    education_history = relationship("ApplicantEducationHistory", back_populates="applicant", uselist=False)
    ssc_marksheet = relationship("SSCMarksheet", back_populates="applicant", uselist=False)
    hsc_marksheet = relationship("HSCMarksheet", back_populates="applicant", uselist=False)
    exam_center = relationship("ExamCenter", back_populates="applicant", uselist=False)
    exam_schedule = relationship("ExamSchedule", back_populates="applicant", uselist=False)
    payment_details = relationship("PaymentDetails", back_populates="applicant", uselist=False)
    admission_result = relationship("AdmissionResult", back_populates="applicant", uselist=False)



class SSCMarksheet(Base):
    __tablename__ = "ssc_marksheet"

    ID = Column(Integer, primary_key=True, index=True)
    Exam_Roll = Column(Integer, ForeignKey("applicant_information.Exam_Roll"), unique=True, nullable=False)
    SSC_GPA = Column(String(5))

    applicant = relationship("ApplicantInformation", back_populates="ssc_marksheet")

class HSCMarksheet(Base):
    __tablename__ = "hsc_marksheet"

    ID = Column(Integer, primary_key=True, index=True)
    Exam_Roll = Column(Integer, ForeignKey("applicant_information.Exam_Roll"), unique=True, nullable=False)
    HSC_GPA = Column(String(5))

    applicant = relationship("ApplicantInformation", back_populates="hsc_marksheet")

