
from sqlalchemy import __version__

from sqlalchemy import create_engine
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import ForeignKey

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.orm import sessionmaker

#from address import Address

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, unique=True)
    name = Column(String)
    fullname = Column(String)
    nickname = Column(String)
    #addresses = relationship("Address", order_by=Address.id, back_populates="user")

    def __init__(self, name, fullname, nickname):
        self.name = name
        self.fullname = fullname
        self.nickname = nickname

engine = create_engine('sqlite:///sqlite/testDB.db', echo=True)
Base.metadata.create_all(bind=engine)
session = sessionmaker(bind=engine)()

row1 = User('Joe', 'Joe Dineen', 'Dindins')
session.add(row1)
session.commit()

#row1.address = ['jdineen21@gmail.com']
#session.commit()



session.close()
