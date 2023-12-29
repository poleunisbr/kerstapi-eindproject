import sqlite3
from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base

# Definieer de naam van je SQLite-databasebestand
DATABASE_NAME = "kerst.db"
SQLALCHEMY_DATABASE_URL = f"sqlite:///{DATABASE_NAME}"

def create_database():
    try:
        conn = sqlite3.connect(DATABASE_NAME)
        cursor = conn.cursor()

        # Maak tabellen voor kerstmarkten, kerstgerechten, kerstdecoraties en gebruikers als deze nog niet bestaan
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS kerstmarkten (
                id INTEGER PRIMARY KEY,
                naam TEXT UNIQUE,
                locatie TEXT,
                datum TEXT
            )
        """)

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS kerstgerechten (
                id INTEGER PRIMARY KEY,
                naam TEXT,
                beschrijving TEXT,
                prijs REAL
            )
        """)

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS kerstdecoraties (
                id INTEGER PRIMARY KEY,
                naam TEXT UNIQUE,
                type TEXT,
                prijs REAL
            )
        """)

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY,
                username TEXT,
                email TEXT UNIQUE
            )
        """)

        conn.commit()
        conn.close()
        print(f"Database {DATABASE_NAME} is aangemaakt of bestaat al.")
    except Exception as e:
        print(f"Fout bij het maken van de database: {str(e)}")

def connect_to_database():
    try:
        conn = sqlite3.connect(DATABASE_NAME)
        return conn
    except Exception as e:
        print(f"Fout bij het verbinden met de database: {str(e)}")
        return None

def close_database(connection):
    if connection:
        connection.close()
        print(f"Databaseverbinding is gesloten.")

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, index=True)
    email = Column(String, unique=True, index=True)

if __name__ == "__main__":
    create_database()
