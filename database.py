import psycopg2
from logger_config import get_logger # Assuming logger_config.py sets up a logger

log = get_logger()

def get_db_connection():
    try:
        conn = psycopg2.connect(
            host="localhost",
            database="myfirstdb",
            user="postgres",
            password="root"
        )
        log.info("Connection established successfully")  # Log successful connection

        return conn
    except psycopg2.Error as e:
        log.error(f"Error connecting to database: {e}")  # Log the error
        return None