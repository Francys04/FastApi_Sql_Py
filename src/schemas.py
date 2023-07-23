import datetime as _dt
"""pydantic is a popular Python library used for data validation and settings management."""
import pydantic as _pydantic

from typing import List

"""create post, when creating the pos will send data just title and content"""
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

"""In the provided code snippet, the Post class seems to be defined as a data model that inherits from _PostBase, 
which is again assumed to be defined elsewhere."""
class Post(_PostBase):
    id: int
    owner_id: int
    date_created: _dt.datetime
    date_last_updated: _dt.datetime

    class Config:
        orm_mode = True


"""The _UserBase class is a Pydantic data model representing the base fields for a User.
Includes an email field of type str. """
class _UserBase(_pydantic.BaseModel):
    email: str


class UserCreate(_UserBase):
    password: str


"""The User class is a Pydantic data model that represents the User entity with additional fields beyond the _UserBase model. 
It inherits from the _UserBase class and includes extra fields like id, is_active, and posts. 
The List[Post] field indicates that a User can have a list of related Post objects."""
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
    