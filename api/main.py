import secrets
from fastapi import FastAPI, HTTPException, Depends, status
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from passlib.context import CryptContext
from datetime import datetime, timedelta
import jose

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
    hashed_password = "$2a$12$KiAqXSH2z3NFSXB.i/rM8uZ.B8WURsVnTWHoaNSGTv007aCQrFak2"

    is_correct_username = creds.username == user
    is_correct_password = pwd_context.verify(creds.password, hashed_password)

    if not (is_correct_username and is_correct_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Onjuiste gebruikersnaam en/of wachtwoord",
            headers={"WWW-Authenticate": "Bearer"},
        )

# Functie om een nieuw JWT-token te genereren
def create_jwt_token(data: dict, expires_delta: timedelta = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, secrets.token_urlsafe(), algorithm="HS256")
    return encoded_jwt

# Token-uitgifte-eindpunt
@app.post("/token")
def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    #Try to authenticate the user
    user = auth.authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=401,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    # Add the JWT case sub with the subject(user)
    access_token = auth.create_access_token(
        data={"sub": user.email}
    )
    #Return the JWT as a bearer token to be placed in the headers
    return {"access_token": access_token, "token_type": "bearer"}

# API-eindpunten
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

@app.get("/users/", response_model=list[schemas.User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    users = crud.get_users(db, skip=skip, limit=limit)
    return users

@app.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    return crud.create_user(db, user)


# Voeg overige eindpunten voor kerstmarkten, kerstgerechten en kerstdecoraties toe op dezelfde manier.

# ...

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
