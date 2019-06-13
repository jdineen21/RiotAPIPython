
from sqlalchemy import create_engine
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Boolean
from sqlalchemy import ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.orm import sessionmaker

from importer import riotApiHandler

from importer.static import Champion
from importer.static import Item
from importer.static import engine

session = sessionmaker(bind=engine)()

championData = riotApiHandler.getChampionData()['data']
itemData = riotApiHandler.getItemData()['data']

for x in championData.keys():
    data = championData[x]
    c = Champion(
        version = data.get('version'),
        id = data.get('id'),
        key = data.get('key'),
        name = data.get('name'),
        title = data.get('title'),
        blurb = data.get('blurb')
    )
    session.add(c)
    session.commit()

for x in itemData.keys():
    data = itemData[x]
    i = Item(
        key = data.get('key'),
        name = data.get('name'),
        description = data.get('description'),
        colloq = data.get('colloq'),
        plaintext = data.get('plaintext')
    )
    session.add(i)
    session.commit()

print ('Initialisation Completed')