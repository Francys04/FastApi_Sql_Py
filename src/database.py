"""sql engine -> database engine is the main service for creating, reading, updating, deleting data 
and protecting the data it collects and interprets SQL commands."""
import sqlalchemy as _sql
""" declarative create a base class for declarative models. This base class is then subclassed 
to create model classes that represent database tables. """
import sqlalchemy.ext.declarative as _declarative
"""SQLAlchemy ORM allows you to define Python classes that map to database tables, 
and it provides a high-level, object-oriented interface for interacting with the database."""
import sqlalchemy.orm as _orm

"""Configuration variable commonly used in Python applications with SQLAlchemy to specify the connection URL for the database"""
SQLALCHEMY_DATABASE_URL = "sqlite:///./database.db"

"""Create an SQLAlchemy engine """
engine = _sql.create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
# engine = create_engine("mysql+mysqldb://scott:tiger@localhost/test")

"""create database sessions"""
SessionLocal = _orm.sessionmaker(autocommit=False, autoflush=False, bind=engine)

"""base class for all SQLAlchemy model classes."""
Base = _declarative.declarative_base()