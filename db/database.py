from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

# SQLALCHEMY_DATABASE_URL = "sqlite:///./fastapi-practice.db"
SQLALCHEMY_DATABASE_URL = "postgresql+psycopg2://postgres:123456@localhost:5432/testingUdemy"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, pool_pre_ping=True
) #connect_args={"check_same_thread": False}
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()