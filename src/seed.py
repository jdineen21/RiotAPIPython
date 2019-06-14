
from importer.match import engine
from importer.row import insertData

from sqlalchemy.orm import sessionmaker
from sqlalchemy import exists

import sqlalchemy.exc

matchDataList = []
with open('match-seed.data', 'r') as file:
    matchDataList = file.read().split('\n')

session = sessionmaker(bind=engine)()

for matchData in matchDataList:
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
