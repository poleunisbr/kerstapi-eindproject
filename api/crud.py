from sqlalchemy.orm import Session
import models
import schemas
import auth

def create_kerstmarkt(db: Session, markt: models.Kerstmarkt):
    db_markt = models.Kerstmarkt(**markt.dict())
    db.add(db_markt)
    db.commit()
    db.refresh(db_markt)
    return db_markt

def read_kerstmarkt(db: Session, markt_id: int):
    return db.query(models.Kerstmarkt).filter(models.Kerstmarkt.id == markt_id).first()

def read_kerstmarkten(db: Session):
    return db.query(models.Kerstmarkt).all()

def update_kerstmarkt(db: Session, markt_id: int, markt: models.Kerstmarkt):
    db_markt = db.query(models.Kerstmarkt).filter(models.Kerstmarkt.id == markt_id).first()
    for key, value in markt.dict().items():
        setattr(db_markt, key, value)
    db.commit()
    db.refresh(db_markt)
    return db_markt

def delete_kerstmarkt(db: Session, markt_id: int):
    db_markt = db.query(models.Kerstmarkt).filter(models.Kerstmarkt.id == markt_id).first()
    if db_markt:
        db.delete(db_markt)
        db.commit()
    return db_markt

def create_kerstgerecht(db: Session, gerecht: models.Kerstgerecht):
    db_gerecht = models.Kerstgerecht(**gerecht.dict())
    db.add(db_gerecht)
    db.commit()
    db.refresh(db_gerecht)
    return db_gerecht

def read_kerstgerecht(db: Session, gerecht_id: int):
    return db.query(models.Kerstgerecht).filter(models.Kerstgerecht.id == gerecht_id).first()

def read_kerstgerechten(db: Session):
    return db.query(models.Kerstgerecht).all()

def update_kerstgerecht(db: Session, gerecht_id: int, gerecht: models.Kerstgerecht):
    db_gerecht = db.query(models.Kerstgerecht).filter(models.Kerstgerecht.id == gerecht_id).first()
    for key, value in gerecht.dict().items():
        setattr(db_gerecht, key, value)
    db.commit()
    db.refresh(db_gerecht)
    return db_gerecht

def delete_kerstgerecht(db: Session, gerecht_id: int):
    db_gerecht = db.query(models.Kerstgerecht).filter(models.Kerstgerecht.id == gerecht_id).first()
    if db_gerecht:
        db.delete(db_gerecht)
        db.commit()
    return db_gerecht

def create_kerstdecoratie(db: Session, decoratie: models.Kerstdecoratie):
    db_decoratie = models.Kerstdecoratie(**decoratie.dict())
    db.add(db_decoratie)
    db.commit()
    db.refresh(db_decoratie)
    return db_decoratie

def read_kerstdecoratie(db: Session, decoratie_id: int):
    return db.query(models.Kerstdecoratie).filter(models.Kerstdecoratie.id == decoratie_id).first()

def read_kerstdecoraties(db: Session):
    return db.query(models.Kerstdecoratie).all()

def update_kerstdecoratie(db: Session, decoratie_id: int, decoratie: models.Kerstdecoratie):
    db_decoratie = db.query(models.Kerstdecoratie).filter(models.Kerstdecoratie.id == decoratie_id).first()
    for key, value in decoratie.dict().items():
        setattr(db_decoratie, key, value)
    db.commit()
    db.refresh(db_decoratie)
    return db_decoratie

def delete_kerstdecoratie(db: Session, decoratie_id: int):
    db_decoratie = db.query(models.Kerstdecoratie).filter(models.Kerstdecoratie.id == decoratie_id).first()
    if db_decoratie:
        db.delete(db_decoratie)
        db.commit()
    return db_decoratie

def create_user(db: Session, user: schemas.UserCreate):
    hashed_password = auth.get_password_hash(user.password)
    db_user = models.User(email=user.email, hashed_password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def read_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()

def read_users(db: Session):
    return db.query(models.User).all()

def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()