from http.client import HTTPException

from sqlalchemy.orm import Session

from db.hash import Hash
from db.models import DbUser
from schemas import UserBase
from fastapi import HTTPException, status

def create_user(db:Session, request:UserBase):
    new_user = DbUser(
        username=request.username,
        email=request.email,
        password= Hash.bcrypt(request.password)
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def get_all_users(db:Session):
    return db.query(DbUser).all()

def get_user(db:Session, user_id:int):
    user= db.query(DbUser).get(user_id)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    return user

def get_user_by_username(db:Session, username:str):
    user= db.query(DbUser).filter(DbUser.username==username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    return user

def update_user(db:Session, request:UserBase, id:int):
    user = db.query(DbUser).get(id)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    user.update({
        DbUser.username: request.username,
        DbUser.email: request.email,
        DbUser.password: Hash.bcrypt(request.password)
    })

    db.commit()
    return 'ok'

def delete_user(db:Session, id:int):
    user = db.query(DbUser).get(id)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    db.delete(user)
    db.commit()
    return 'user deleted'