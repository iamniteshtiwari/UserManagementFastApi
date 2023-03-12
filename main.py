from fastapi import FastAPI,Depends
from user import schemas,hashing
from user import models
from user.database import engine,SessionLocal
from sqlalchemy.orm import Session
from passlib.context import CryptContext
from user.hashing import Hash

from user.routers import post, user,auth


app=FastAPI()


models.Base.metadata.create_all(engine)
def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()



@app.post('/user')
def create(request: schemas.User,db: Session =Depends(get_db)):
   
    new_user=models.User(name=request.name,email=request.email,password=Hash.bcrypt(request.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

app.include_router(auth.router)
app.include_router(post.router)
app.include_router(user.router)