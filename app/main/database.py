from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker
import os


engine = create_engine(os.environ.get('DEV_DB_URL'))
Base = declarative_base()
Base.metadata.reflect(engine)

def get_session():
    return scoped_session(sessionmaker(bind=engine))
