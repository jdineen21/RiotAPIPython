
from importer.match import engine
from importer.row import insertData

from sqlalchemy.orm import sessionmaker
from sqlalchemy import exists

import ast
import json
import sqlalchemy.exc

matchDataList = []
with open('match-seed.data', 'r') as file:
    matchDataList = file.read().split('\n')

print len(matchDataList)

session = sessionmaker(bind=engine)()

for i in range(len(matchDataList)):
    matchData = ast.literal_eval(matchDataList[i])
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

session.close()