from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from .. import models 




def create_blog(db:Session, request):
    new_blog = models.Blog(title=request.title, body=request.body, user_id=2)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog) 
    return new_blog


def allblogs(db:Session, request):
    params = request.query_params
    if params.get('id'):
        blogs = db.query(models.Blog).get(params.get('id'))
    else:
        blogs = db.query(models.Blog).all()
    return blogs


def getblog(id:int, db:Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"blog with the Id {id} is not Available.")

        # response.status_code = status.HTTP_404_NOT_FOUND
        # return {'detail': f"blog with the Id {id} is not Available."}
    return blog

def deleteblog(id:int, db:Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= f"Blog id {id} Not Found.")
    
    blog.delete(synchronize_session=False)
    db.commit()
    return {"detail": "Delete successful"}


def updateblog(id:int,request, db: Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog id {id} Not found")
    
    # blog_data = request.dict(exclude_unset=True)
    # blog.update(blog_data, synchronize_session=False)
    blog.update(dict(request))
    db.commit()
    return "Update.."