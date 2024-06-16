from pydantic import BaseModel
from typing import List



class Blog(BaseModel):
    title : str
    body : str
    
## Return all fields in Blog
# class ShowBlog(Blog):
#     class Config:
#         orm_mode = True   ## its optional


class User(BaseModel):
    name : str
    email : str
    password : str
    

class ShowUser(BaseModel):
    name : str
    email : str
    
    # blogs : List[Blog]
    
class ShowUserRel(BaseModel):
    name : str
    email : str
    
        
## Return given fields only 
class ShowBlog(BaseModel):
    title: str
    body : str  
    creator : ShowUserRel
    
        
        
class Login(BaseModel):
    username : str
    password : str
    
    
    
## JWT Token

class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: str | None = None