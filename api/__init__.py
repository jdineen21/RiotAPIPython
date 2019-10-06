
import urllib
import json
import requests
import time

delay = 0.9

def getFeaturedGames():
    time.sleep(delay)
    r = requests.get('http://127.0.0.1:5002/featured-games')
    if r.status_code != 200:
        return None
    
    return json.loads(r.content)

def getMatchById(matchId):
    time.sleep(delay)
    r = requests.get('http://127.0.0.1:5002/match/%s' % (matchId))
    if r.status_code != 200:
        return None
    
    return json.loads(r.content)

def getMatchTimelineById(matchId):
    time.sleep(delay)
    r = requests.get('http://127.0.0.1:5002/timeline/%s' % (matchId))
    if r.status_code != 200:
        return None
    
    return json.loads(r.content)

def getMatchlistsBySummonerId(summonerId):
    time.sleep(delay)
    r = requests.get('http://127.0.0.1:5002/matchlists/%s' % (summonerId))
    if r.status_code != 200:
        return None
    
    return json.loads(r.content)

def getSummonerBySummonerName(summonerName):
    time.sleep(delay)
    r = requests.get('http://127.0.0.1:5002/summoner/%s' % (summonerName))
    if r.status_code != 200:
        return None
    
    return json.loads(r.content)