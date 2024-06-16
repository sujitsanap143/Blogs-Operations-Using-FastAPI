from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base


class Blog(Base):
    __tablename__ = 'blogs'
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(50))
    body = Column(String(200))
    user_id = Column(Integer, ForeignKey("users.id"))
    
    creator = relationship("User", back_populates='blogs')
    


class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(30))
    email = Column(String(30))
    password = Column(String(200))
    
    blogs = relationship("Blog", back_populates="creator")