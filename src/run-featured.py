from importer.match import engine
from importer.match import Match
from importer.row import insertData
from importer import riotApiHandler

from sqlalchemy.orm import sessionmaker
from sqlalchemy import exists

import sqlalchemy.exc

session = sessionmaker(bind=engine)()
print ('Initialisation Completed')

while True:
    featuredGames = riotApiHandler.getFeaturedGames()
    for x in range(len(featuredGames['gameList'])):
        gameId = featuredGames['gameList'][x]['gameId']
        if not session.query(exists().where(Match.gameId==gameId)).scalar():
            matchData = riotApiHandler.getMatchById(gameId)
            while matchData is None:
                matchData = riotApiHandler.getMatchById(gameId)

            with open('match-seed.data', 'a') as file:
                file.write(str(matchData)+'\n')

            row = insertData(session, matchData)

            try:
                if ('9.13' in matchData.get('gameVersion')):
                    session.add(row)
                    session.commit()
                    print 'Data Inserted'
                else:
                    print 'Data from old Patch'
            except sqlalchemy.exc.IntegrityError as e:
                print 'Integrity Error'
                session.rollback()
            except Exception as e:
                print 'Error on commit'
                print e
                pass
        else:
            print 'Skip ovelapping match data!'
