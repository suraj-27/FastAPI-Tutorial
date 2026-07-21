from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

# Database URL
# Format:
# sqlite:///./database_name.db
# Three slashes mean the database file is in the current project directory.
SQLALCHEMY_DATABASE_URL = "sqlite:///./blog.db"

#----------------------------------------------------------
# Create the database engine
# The engine is responsible for managing the connection
# between python application and sqlite database
#----------------------------------------------------------
engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread":False},
)

#----------------------------------------------------
#
# Create session factory
#
# SessionLocal is not session
# It will create new session
#
# Every API request will create its own session
#----------------------------------------------------
SessionLocal = sessionmaker(autoflush=False, autocommit=False, bind=engine)


#--------------------------------------------------
# Base class for all ORM models
#
# Every Sqlalchemy table should inherit from base
#--------------------------------------------------
class Base(DeclarativeBase):
    pass

#--------------------------------------------------
# Dependency function  used in Fastapi
#
# Create one database session per request
# After the request finishes, the session is
# close automatically.
#---------------------------------------------------
def get_db():
    with SessionLocal() as db:
        yield db