
from sqlalchemy import create_engine
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Boolean
from sqlalchemy import ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.orm import sessionmaker

Base = declarative_base()
engine = create_engine('sqlite:///sqlite/main.db')

class Champion(Base):

    __tablename__ = 'champions'

    version = Column(String)
    id = Column(String)
    key = Column(Integer, primary_key=True)
    name = Column(String)
    title = Column(String)
    blurb = Column(String)

class Item(Base):

    __tablename__ = 'items'

    key = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)
    colloq = Column(String)
    plaintext = Column(String)

Base.metadata.create_all(bind=engine)