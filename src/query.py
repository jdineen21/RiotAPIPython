
from importer.match import engine
from importer.match import Match
from importer.match import Player
from importer.match import Participant
from importer.match import Stats
from importer.match import Team
from importer.match import Ban

from importer.static import Champion
from importer.static import Item

from sqlalchemy.orm import sessionmaker

import statistics

session = sessionmaker(bind=engine)()

result = session.query(Match.gameDuration).filter(Match.gameMode == 'CLASSIC')
time = []
for row in result:
    time.append(row[0])

print sum(time)/len(time)/60

result = session.query(Stats.totalDamageDealt).join(Participant, Stats.id==Participant.id).join(Match, Participant.gameId==Match.gameId).filter(Match.gameMode=='ARAM')
time = []
for row in result:
    time.append(row[0])

print sum(time)/len(time)
