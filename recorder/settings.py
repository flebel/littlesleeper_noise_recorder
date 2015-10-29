from distutils.util import strtobool
from os import environ

DB_URI = 'sqlite:///db.sqlite'
DEBUG = strtobool(environ.get('DEBUG', 'False'))

