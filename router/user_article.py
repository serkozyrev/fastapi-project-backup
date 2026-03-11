from typing import List

from fastapi import APIRouter
from fastapi.params import Depends
from sqlalchemy.orm import Session
from auth.oAuth2 import oAuth2_schema, get_current_user

from db import db_article
from db.database import get_db
from schemas import ArticleBase, ArticleDisplay, UserBase

router = APIRouter(
    prefix="/article",
    tags=["article"]
)

#create user
@router.post("/", response_model=ArticleDisplay)
def create_article(request:ArticleBase, db:Session=Depends(get_db), current_user:UserBase=Depends(get_current_user)):
    return db_article.create_article(db, request)

#read user
# @router.get('/', response_model=List[ArticleDisplay])
# def get_all_articles(db:Session=Depends(get_db)):
#     return db_article.get_all_users(db)

@router.get("/{article_id}") #, response_model=ArticleDisplay
def get_article(article_id:int, db:Session=Depends(get_db), current_user:UserBase=Depends(get_current_user)):
    return {'data': db_article.get_article(db, article_id), 'current_user': current_user}