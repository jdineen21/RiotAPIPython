from importer.match import engine
from importer.match import Match
from importer.row import insertData
from importer import riotApiHandler

from sqlalchemy.orm import sessionmaker
from sqlalchemy import exists

import sqlalchemy.exc

session = sessionmaker(bind=engine)()
print ('Initialisation Completed')

for loop in range(25):
    featuredGames = riotApiHandler.getFeaturedGames()
    for x in range(len(featuredGames['gameList'])):
        for y in range(len(featuredGames['gameList'][x]['participants'])):
            summonerName = featuredGames['gameList'][x]['participants'][y]['summonerName']
            print summonerName
            summonerId = riotApiHandler.getSummonerBySummonerName(summonerName)['accountId']
            print summonerId
            matchlists = riotApiHandler.getMatchlistsBySummonerId(summonerId)['matches']
            for z in range(len(matchlists)):
                if not session.query(exists().where(Match.gameId==matchlists[z]['gameId'])).scalar():
                    matchData = riotApiHandler.getMatchById(matchlists[z]['gameId'])
                    while matchData is None:
                        matchData = riotApiHandler.getMatchById(matchlists[z]['gameId'])

                    with open('match-seed.data', 'a') as file:
                        file.write(str(matchData)+'\n')

                    row = insertData(session, matchData)

                    try:
                        session.add(row)
                        session.commit()
                        print 'Data Inserted'
                    except sqlalchemy.exc.IntegrityError as e:
                        print 'Integrity Error'
                        session.rollback()
                    except Exception as e:
                        print 'Error on commit'
                        print e
                        pass
                else:
                    print 'Skip ovelapping match data!'