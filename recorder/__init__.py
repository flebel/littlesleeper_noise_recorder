from distutils.util import strtobool
from os import environ

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DEBUG = strtobool(environ.get('DEBUG', 'False'))

engine = create_engine('sqlite:///db.sqlite', echo=DEBUG)
session = sessionmaker(bind=engine)()

