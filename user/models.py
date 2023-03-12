from sqlalchemy import Column,Integer,String, ForeignKey
from user.database import Base
from sqlalchemy.orm import relationship




class User(Base):
    __tablename__='users'
    id= Column(Integer,primary_key=True,index=True)
    name=Column(String)
    email=Column(String)
    password=Column(String)

    posts= relationship('Post',back_populates="creator")


class Post(Base):
    __tablename__ ="posts"
    id= Column(Integer,primary_key=True,index=True)
    title=Column(String)
    body = Column(String)
    user_id=Column(Integer,ForeignKey('users.id'))
    

    creator =relationship("User",back_populates="posts")