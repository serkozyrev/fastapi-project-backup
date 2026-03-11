from typing import List

from pydantic import BaseModel

#Article inside UserDisplay
class Article(BaseModel):
    title: str
    content: str
    published: bool
    class ConfigDict:
        from_attributes=True

class UserBase(BaseModel):
    username: str
    email:str
    password:str

class UserDisplay(BaseModel):
    username:str
    email:str
    items: List[Article] =[]
    class ConfigDict:
        from_attributes=True

class ArticleBase(BaseModel):
    title: str
    content: str
    published: bool
    creator_id: int

#User inside Article Display
class User(BaseModel):
    id:int
    username: str
    class ConfigDict:
        from_attributes=True

class ArticleDisplay(BaseModel):
    title: str
    content: str
    published: bool
    user:User
    class ConfigDict:
        from_attributes=True