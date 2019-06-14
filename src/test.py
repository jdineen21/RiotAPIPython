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

result = session.query(Participant.championId).join(Match).filter(Match.gameMode=='ARAM')
for row in result:
    print row[0]