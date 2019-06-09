
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Table, Integer, String, ForeignKey

from player import Player

Base = declarative_base()

class ParticipantIdentity(Base):
    participantId = Column(Integer)
    player = relationship('Player', Player())
