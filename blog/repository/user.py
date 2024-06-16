from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from .. import models, hashing, schemas

def createuser(db:Session, request: schemas.User):
    new_user = models.User(name=request.name, email=request.email, password=hashing.Hash.bcrypt(request.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


def alluser(db:Session):
    user = db.query(models.User).all()
    return user



def getuser(id: int, db:Session):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"{id} User not Available.")
    
    return user