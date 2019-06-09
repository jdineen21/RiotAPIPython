
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()

class Player(Base):
    accountId = Column(String)
    currentAccountId = Column(String)
    currentPlatformId = Column(String)
    matchHistoryUri = Column(String)
    platformId = Column(String)
    profileIcon = Column(Integer)
    summonerId = Column(String)
    summonerName = Column(String)