import secrets
from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from passlib.context import CryptContext

import crud
import database
from schemas import Kerstmarkt, Kerstgerecht, Kerstdecoratie

app = FastAPI()

# OAuth2 met wachtwoordverificatie
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Afhankelijkheid om een SQLAlchemy-sessie te verkrijgen
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Maak een instantie van CryptContext voor wachtwoordhashing
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Basis authenticatie
def authenticate(creds: OAuth2PasswordRequestForm = Depends()):
    user = "administrator"
    hashed_password = "$2a$12$lCKpa42/Pnat/cjtgrVpUOxmFtV4JcPo0ORur.2a4sGzhJfYnC10i"

    is_correct_username = creds.username == user
    is_correct_password = pwd_context.verify(creds.password, hashed_password)

    if not (is_correct_username and is_correct_password):
        raise HTTPException(
            status_code=401,
            detail="Onjuiste gebruikersnaam en/of wachtwoord",
            headers={"WWW-Authenticate": "Bearer"},
        )

# API-eindpunten voor kerstmarkten
@app.post("/kerstmarkten/", response_model=Kerstmarkt)
def create_kerstmarkt(
    markt: Kerstmarkt,
    db: Session = Depends(get_db),
    creds: OAuth2PasswordRequestForm = Depends(oauth2_scheme)
):
    authenticate(creds)
    return crud.create_kerstmarkt(db, markt)

@app.get("/kerstmarkten/{markt_id}", response_model=Kerstmarkt)
def read_kerstmarkt(markt_id: int, db: Session = Depends(get_db)):
    kerstmarkt = crud.read_kerstmarkt(db, markt_id)
    if kerstmarkt is None:
        raise HTTPException(status_code=404, detail="Kerstmarkt niet gevonden")
    return kerstmarkt

# Voeg overige eindpunten voor kerstmarkten, kerstgerechten en kerstdecoraties toe op dezelfde manier.

# ...

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
