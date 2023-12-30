from pydantic import BaseModel


class Kerstmarkt(BaseModel):
    id: int
    naam: str
    locatie: str
    datum: str


class Kerstgerecht(BaseModel):
    id: int
    naam: str
    beschrijving: str
    prijs: float


class Kerstdecoratie(BaseModel):
    id: int
    naam: str
    type: str
    prijs: float

class User(BaseModel):
    username: str
    email: str


class UserCreate(BaseModel):
    username: str
    email: str
    password: str
