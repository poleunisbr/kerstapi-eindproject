from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import relationship
from database import Base


class Kerstmarkt(Base):
    __tablename__ = "kerstmarkten"
    id = Column(Integer, primary_key=True, index=True)
    naam = Column(String, unique=True, index=True)
    locatie = Column(String)
    datum = Column(String)

class Kerstgerecht(Base):
    __tablename__ = "kerstgerechten"
    id = Column(Integer, primary_key=True, index=True)
    naam = Column(String, index=True)
    beschrijving = Column(String)
    prijs = Column(Float)

class Kerstdecoratie(Base):
    __tablename__ = "kerstdecoraties"
    id = Column(Integer, primary_key=True, index=True)
    naam = Column(String, unique=True, index=True)
    type = Column(String)
    prijs = Column(Float)

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, index=True)
    email = Column(String, index=True)
