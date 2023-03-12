from pydantic import BaseModel
from typing import List, Optional

class PostBase(BaseModel):
    title:str
    body: str
    user_id:int
    

class Post(PostBase):
    class Config():
        orm_mode=True


class User(BaseModel):
    name:str
    email:str
    password:str

class ShowUser(BaseModel):
    name:str
    email:str
    posts :List[Post]=[]
    class Config():
        orm_mode=True

class ShowPost(BaseModel):
    title:str
    body:str
    creator: ShowUser

    class Config():
        orm_mode=True

class Login(BaseModel):
    username:str
    password:str

class Token(BaseModel):
    access_token:str
    token_type:str


class Tokendata(BaseModel):
    email:Optional[str]=None
    

