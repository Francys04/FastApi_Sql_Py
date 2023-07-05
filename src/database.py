import sqlalchemy as _sql

import sqlalchemy.ext.declarative as _declarative
import sqlalchemy.orm as _orm 

SQLALCHEMY_DATABASE_URL = "sqllite:///./database.db"


# sql engine
# he database engine is the main service for creating, reading, 
# updating, deleting data and protecting the data it collects and interprets SQL commands.

engine = _sql.create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})

SessionLocal = _orm.sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = _declarative.declarative_base()