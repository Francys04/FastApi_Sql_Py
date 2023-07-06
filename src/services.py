import database as _db, models as _models, schemas as _schemas
from sqlalchemy import *
import sqlalchemy.orm as _orm
import datetime as _dt



metadata = MetaData()
# create db
def create_database():
    return _db.Base.metadata.create_all(bind=_db.engine)


# create sesion local with close db
def get_db():
    db = _db.SessionLocal()
    try:
        yield db
    finally:
        db.close()

# get data from user by email, return list
def get_user_by_email(db:_orm.Session, email:str):
    return db.query(_models.User).filter(_models.User.email == email).first()


# create user
def create_user(db: _orm.Session, user:_schemas.UserCreate):
    fake_hashed_passw = user.password + "thisisnotsecure"
    db_user = _models.User(email=user.email, hashed_password=fake_hashed_passw)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user



# create service for get user
def get_users(db: _orm.Session, skip:int , limit:int):
    return db.query(_models.User).offset(skip).limit(limit).all()

# example
# {
#     "apple", "orange", "pineaple"
# }

# get user single ojs
# first() retrieve the first result that matches the query criteria. 
# It returns a single instance of the Post model, or None if no matching result is found.

# filter() This line adds a filter to the query. It specifies a condition that narrows down the results based on the id column of 
# the Post table. post_id is likely a variable holding the specific id value you want to search for.
def get_user(db: _orm.Session, user_id:int):
    return db.query(_models.User).filter(_models.User.id == user_id).first()


# get create a post
def create_post(db: _orm.Session, post: _schemas.PostCreate, user_id: int):
    post = _models.Post(**post.dict(), owner_id=user_id)
    db.add(post)
    db.commit()
    db.refresh(post)
    return post


# for read post fun
def get_posts(db: _orm.Session, skip: int, limit: int):
    return db.query(_models.Post).offset(skip).limit(limit).all()


# idividual post
def get_post(db: _orm.Session, post_id: int):
    return db.query(_models.Post).filter(_models.Post.id == post_id).first()

# delete post
def delete_post(db: _orm.Session, post_id: int):
    db.query(_models.Post).filter(_models.Post.id == post_id).first()
    
    
# update post
def update_post(db: _orm.Session,post: _schemas.PostCreate, post_id:int):
    db_post = get_post(db=db, post_id = post_id)
    db.post.title = post.title
    db_post.content = post.content
    db_post.date_last_updated = _dt.datetime.now
    db.commit()
    db.refresh(db_post)
    return db_post

