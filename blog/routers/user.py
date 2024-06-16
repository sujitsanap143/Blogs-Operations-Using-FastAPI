from fastapi import APIRouter, Depends
from .. import database, schemas
from sqlalchemy.orm import Session
from ..repository import user



router = APIRouter(
    prefix="/api",
    tags=['Users']
)


get_db = database.get_db

@router.post('/user', response_model=schemas.ShowUser)
def create_user(request : schemas.User, db: Session = Depends(get_db)):
    return user.createuser(db, request)


@router.get('/users', response_model=list[schemas.ShowUser])
def all_users(db:Session=Depends(get_db)):
    return user.alluser(db)



@router.get('/users/{id}', response_model=schemas.ShowUser)
def get_user(id, db:Session=Depends(get_db)):
    return user.getuser(id, db)