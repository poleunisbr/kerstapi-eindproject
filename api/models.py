from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_NAME = "kerst.db"
SQLALCHEMY_DATABASE_URL = f"sqlite:///{DATABASE_NAME}"

engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def create_database():
    Base.metadata.create_all(bind=engine)
    print(f"Database {DATABASE_NAME} is aangemaakt of bestaat al.")

def connect_to_database():
    return engine.connect()

def close_database(connection):
    if connection:
        connection.close()
        print(f"Databaseverbinding is gesloten.")

if __name__ == "__main__":
    create_database()
