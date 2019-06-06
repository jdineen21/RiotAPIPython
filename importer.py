
import urllib
import json
import time
import csv
import hashlib

import mysql.connector
import riotApiHandler

mydb = mysql.connector.connect(
    host="localhost",
    user="admin",
    passwd="badger77"
)

print mydb.is_connected()

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

        for iter in range(len(participants)):
            summonerId = riotApiHandler.getSummonerBySummonerName(participants[iter]['summonerName'])['accountId']
            matchlists = riotApiHandler.getMatchlistsBySummonerId(summonerId)
            for match in range(len(matchlists['matches'])):
                print riotApiHandler.neatenJson(riotApiHandler.getMatchById(matchlists['matches'][match]['gameId']))

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