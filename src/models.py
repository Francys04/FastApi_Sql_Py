"""Python SQL toolkit and Object Relational Mapper that gives application developers the full power and flexibility of SQL."""
import sqlalchemy as _sql
""" "bridge" between object-oriented programs and, in most cases, relational databases"""
import sqlalchemy.orm as _orm 

import database as _database
"""The datetime module provides classes for manipulating dates and times in both simple and complex ways."""
import datetime as _dt


"""table for user data"""
class User(_database.Base):
    __tablename__ = "users"
    id = _sql.Column(_sql.Integer, primary_key=True)
    email = _sql.Column(_sql.String, unique=True, index=True)
    hashed_password = _sql.Column(_sql.String)
    is_active = _sql.Column(_sql.Boolean, default=True)
    
    
    posts = _orm.relationship("Post", back_populates="owner")
    
"""table for post data"""
class Post(_database.Base):
    __tablename__ = "posts"
    id = _sql.Column(_sql.Integer, primary_key=True, index=True)
    title = _sql.Column(_sql.String, index=True)
    content = _sql.Column(_sql.String, index=True)
    owner_id = _sql.Column(_sql.Integer, _sql.ForeignKey("users.id"))
    date_created = _sql.Column(_sql.DateTime, default=_dt.datetime.utcnow)
    date_last_updated = _sql.Column(_sql.DateTime, default=_dt.datetime.utcnow)
    
    owner = _orm.relationship("User", back_populates="posts")
    
    