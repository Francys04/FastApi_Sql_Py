import datetime as _dt

import pydantic as _pydantic

from typing import List

# create post, when creating the pos will send data just title and content
class _PostBase(_pydantic.BaseModel):
    title:str
    content:str

# api functionality schemas
# {
#     "id":1,
#     "owner_id":23,
#     "title":"this is a title",
#     "content":"this is an content",
#     "date_created":"12-12-12",
#     "date_last_updated":"12-12-12"
# }
 

class PostCreate(_PostBase):
    pass


class Post(_PostBase):
    id: int
    owner_id: int
    date_created: _dt.datetime
    date_last_updated: _dt.datetime

    class Config:
        orm_mode = True


class _UserBase(_pydantic.BaseModel):
    email: str


class UserCreate(_UserBase):
    password: str


class User(_UserBase):
    id: int
    is_active: bool
    posts: List[Post] = []

    class Config:
        orm_mode = True
        
        
        
#  {
#   "email": "string@gmail.com",
#   "id": 5,
#   "is_active": true,
#   "posts": []
# }   
    