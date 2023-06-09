from typing import List
from fastapi import APIRouter, Depends, status, HTTPException
from user import schemas, database, models, oauth2
from sqlalchemy.orm import Session
from user.repo import post

router = APIRouter(
    prefix="/post",
    tags=['Posts']
)

get_db = database.get_db


@router.get('/', response_model=List[schemas.ShowPost])
def all(db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return post.get_all(db)


@router.post('/', status_code=status.HTTP_201_CREATED,)
def create(request: schemas.Post, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return post.create(request, db)


@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def destroy(id: int, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return post.destroy(id, db)


@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def update(id: int, request: schemas.Post, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return post.update(id, request, db)


@router.get('/{id}', status_code=200, response_model=schemas.ShowPost)
def show(id: int, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return post.show(id, db)
