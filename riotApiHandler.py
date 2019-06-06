
from ratelimit import limits, RateLimitException, sleep_and_retry

import urllib
import json
import requests

@sleep_and_retry
@limits(calls=3, period = 1)
def getFeaturedGames():
    r = requests.get('https://euw1.api.riotgames.com/lol/spectator/v4/featured-games?api_key=RGAPI-eb2d12a4-fb4e-4c6c-b621-4b2fa15e0208')
    #print r.headers
    if r.status_code == 429:
        print 'EXCEEDED'
    else:
        return r.json()

@sleep_and_retry
@limits(calls=3, period = 1)
def getMatchById(matchId):
    r = requests.get('https://euw1.api.riotgames.com/lol/match/v4/matches/%s?api_key=RGAPI-eb2d12a4-fb4e-4c6c-b621-4b2fa15e0208' % (matchId))
    #print r.headers
    if r.status_code == 429:
        print 'EXCEEDED'
    else:
        return r.json()

@sleep_and_retry
@limits(calls=1, period = 2)
def getMatchlistsBySummonerId(summonerId):
    r = requests.get('/lol/match/v4/matchlists/by-account/%s?api_key=RGAPI-eb2d12a4-fb4e-4c6c-b621-4b2fa15e0208' % (summonerId))
    #print r.headers
    if r.status_code == 429:
        print 'EXCEEDED'
    else:
        return r.json()

@sleep_and_retry
@limits(calls=1, period = 2)
def getSummonerBySummonerName(summonerName):
    escapedSummonerName = urllib.quote(summonerName.encode('utf -8'))
    url = 'https://euw1.api.riotgames.com/lol/summoner/v4/summoners/by-name/' + escapedSummonerName  + '?api_key=RGAPI-eb2d12a4-fb4e-4c6c-b621-4b2fa15e0208'
    r = requests.get(url)
    #print r.headers
    if r.status_code == 429:
        print 'EXCEEDED'
    else:
        return r.json()