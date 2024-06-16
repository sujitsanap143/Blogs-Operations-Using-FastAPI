from fastapi import APIRouter, Request, Depends, status
from typing import List
from .. import schemas, database
from sqlalchemy.orm import Session
from ..repository import blog
from .. import oauth2

router = APIRouter(
    prefix="/api",
    tags=['Blogs'],
    
)



get_db = database.get_db

@router.post('/blog', status_code=status.HTTP_201_CREATED)
def create(request: schemas.Blog, db: Session = Depends(get_db)):
    return blog.create_blog(db, request)


@router.get('/blogs', response_model=List[schemas.ShowBlog])
def get_all_blogs( request: Request, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.allblogs(db, request)

## return all blog.
# @app.get('/api/blogs')
# def get_all_blogs(db: Session = Depends(get_db)):
#     blogs = db.query(models.Blog).all()
#     return blogs


## get blog by id.
@router.get('/blogs/{id}', response_model=schemas.ShowBlog)
def get_by_id(id, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.getblog(id, db)



@router.delete('/blogs/{id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_blog(id, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.deleteblog(id, db)
    
    
    
@router.put('/blogs/{id}', status_code=status.HTTP_202_ACCEPTED)
def update_blog(id, request: schemas.Blog, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.updateblog(id, request, db)
 