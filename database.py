from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from logger_config import get_logger

log = get_logger("database_logger")

# Database connection string (SQLAlchemy format)
DATABASE_URL = "postgresql://postgres:root@localhost/myfirstdb"

# Create engine
try:
    engine = create_engine(DATABASE_URL, echo=False)
    log.info("SQLAlchemy engine created successfully")
except Exception as e:
    log.error(f"Error creating SQLAlchemy engine: {e}")
    engine = None

# Create session factory
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db_connection():
    """Get a database session"""
    try:
        if engine is None:
            log.error("Engine is not initialized")
            return None
        
        session = SessionLocal()
        log.info("Database session established successfully")
        return session
    except Exception as e:
        log.error(f"Error establishing database session: {e}")
        return None

def get_db():
    """Dependency for FastAPI/Flask applications"""
    db = get_db_connection()
    try:
        yield db
    finally:
        if db:
            db.close()
            log.info("Database session closed")


