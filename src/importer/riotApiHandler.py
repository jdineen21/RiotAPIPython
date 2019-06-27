
from ratelimit import limits, RateLimitException, sleep_and_retry

import urllib
import json
import requests
import time

api_key = 'RGAPI-3f73c12d-564e-4fc1-a9fc-985064e208f1'

HTTP_STATUS_CODES = {
400:	'Bad request',
401:	'Unauthorized',
403:	'Forbidden',
404:	'Data not found',
405:	'Method not allowed',
415:	'Unsupported media type',
429:	'Rate limit exceeded',
500:	'Internal server error',
502:	'Bad gateway',
503:	'Service unavailable',
504:	'Gateway timeout'
}

def neatenJson(raw_json):
    return json.dumps(raw_json, indent=4, sort_keys=True)

@sleep_and_retry
@limits(calls=1, period = 2)
def getFeaturedGames():
    r = requests.get('https://euw1.api.riotgames.com/lol/spectator/v4/featured-games?api_key=%s' % (api_key))
    if r.status_code in HTTP_STATUS_CODES:
        print 'getFeaturedGames: %s' % HTTP_STATUS_CODES[r.status_code]
        time.sleep(20)
        getFeaturedGames()
    else:
        return r.json()

@sleep_and_retry
@limits(calls=1, period = 2)
def getMatchById(matchId):
    url = 'https://euw1.api.riotgames.com/lol/match/v4/matches/%s?api_key=%s' % (matchId, api_key)
    r = requests.get(url)
    if r.status_code in HTTP_STATUS_CODES:
        print 'getMatchById: %s' % HTTP_STATUS_CODES[r.status_code]
        time.sleep(20)
        getMatchById(matchId)
    else:
        return r.json()

@sleep_and_retry
@limits(calls=1, period = 2)
def getMatchlistsBySummonerId(summonerId):
    escapedSummonerId = urllib.quote(summonerId.encode('utf -8'))
    url = 'https://euw1.api.riotgames.com/lol/match/v4/matchlists/by-account/%s?api_key=%s' % (escapedSummonerId, api_key)
    r = requests.get(url)
    if r.status_code in HTTP_STATUS_CODES:
        print 'getMatchlistsBySummonerId: %s' % HTTP_STATUS_CODES[r.status_code]
        time.sleep(20)
        getMatchlistsBySummonerId(summonerId)
    else:
        return r.json()

@sleep_and_retry
@limits(calls=1, period = 2)
def getSummonerBySummonerName(summonerName):
    escapedSummonerName = urllib.quote(summonerName.encode('utf -8'))
    url = 'https://euw1.api.riotgames.com/lol/summoner/v4/summoners/by-name/%s?api_key=%s' % (escapedSummonerName, api_key)
    r = requests.get(url)
    if r.status_code in HTTP_STATUS_CODES:
        print 'getSummonerBySummonerName: %s' % HTTP_STATUS_CODES[r.status_code]
        time.sleep(20)
        getSummonerBySummonerName(summonerName)
    else:
        return r.json()

def getChampionData():
    r = requests.get('http://ddragon.leagueoflegends.com/cdn/9.12.1/data/en_US/champion.json?api_key=%s' % (api_key))
    if r.status_code in HTTP_STATUS_CODES:
        print 'getChampionData: %s' % HTTP_STATUS_CODES[r.status_code]
        time.sleep(20)
        getFeaturedGames()
    else:
        return r.json()

def getItemData():
    r = requests.get('http://ddragon.leagueoflegends.com/cdn/9.12.1/data/en_US/item.json?api_key=%s' % (api_key))
    if r.status_code in HTTP_STATUS_CODES:
        print 'getItemData: %s' % HTTP_STATUS_CODES[r.status_code]
        time.sleep(20)
        getFeaturedGames()
    else:
        return r.json()
