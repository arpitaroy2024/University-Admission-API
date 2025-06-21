from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# MySQL Connection URL (Update with your credentials)
URL_DATABASE = "mysql+pymysql://mysql:mysql@localhost/ju_admission_406"

# Create database engine
engine = create_engine(URL_DATABASE)

# Session for database operations
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for models
Base = declarative_base()
