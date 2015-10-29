from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

import settings

engine = create_engine(settings.DB_URI, echo=settings.DEBUG)
session = sessionmaker(bind=engine)()

