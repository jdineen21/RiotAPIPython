
from importer.match import engine
from importer.match import Match
#from importer.match import ParticipantIdentity
from importer.match import Player
from importer.match import Participant
from importer.match import Stats
from importer.match import Team
from importer.match import Ban

from importer.static import Champion
from importer.static import Item

from sqlalchemy.orm import sessionmaker

session = sessionmaker(bind=engine)()

result = session.query(Match).filter(Match.gameMode == 'CLASSIC')
games = []
for row in result:
    games.append(row.gameId)
print len(games)