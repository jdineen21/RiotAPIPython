
import urllib
import json
import time
import csv
import hashlib
import mysql.connector
import riotApiHandler

from match import *


mydb = mysql.connector.connect(
    host="localhost",
    user="admin",
    passwd="badger77"
)

print 'DB Connected: %s' % (mydb.is_connected())

while True:
    cache = {}

    featured_games = riotApiHandler.getFeaturedGames()

    for i in range(len(featured_games['gameList'])):
        game = featured_games['gameList'][i]
        bannedChampions = game['bannedChampions']
        gameId = game['gameId']
        gameLength = game['gameLength']
        gameMode = game['gameMode']
        gameQueueConfigId = game['gameQueueConfigId']
        gameStartTime = game['gameStartTime']
        gameType = game['gameType']
        mapId = game['mapId']
        observers = game['observers']
        participants = game['participants']
        platformId = game['platformId']

        for x in range(len(participants)):
            summonerId = riotApiHandler.getSummonerBySummonerName(participants[x]['summonerName'])['accountId']
            matchlists = riotApiHandler.getMatchlistsBySummonerId(summonerId)
            for y in range(len(matchlists['matches'])):
                matchData = riotApiHandler.getMatchById(matchlists['matches'][y]['gameId'])
                m = Match(matchData)

                mydb.commit
                #mydb.prepare_for_mysql
                

            #print riotApiHandler.neatenJson(matchlists)
    



    #print participants

    #match = riotApiHandler.getMatchById(gameId)
    #print match

#print type(featured_games)

#mydb = mysql.connector.connect(
#    host="localhost",
#    user="admin",
#    passwd="badger77"
#)

#print(mydb)