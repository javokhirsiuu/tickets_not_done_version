from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.engine import create_engine



my_sqlalchemy_url = ("postgresql://postgres:java2103@localhost:5432/Twitter")

engine = create_engine(my_sqlalchemy_url)
Session_LOCAL = sessionmaker(autoflush=False,autocommit=False,bind=engine)
Base = declarative_base()




def get_db():
    global db
    try:
        db = Session_LOCAL()
        yield db
    finally:
        db.close()