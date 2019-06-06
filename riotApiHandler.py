
from ratelimit import limits, RateLimitException, sleep_and_retry

import urllib
import json
import requests

api_key = 'RGAPI-eb2d12a4-fb4e-4c6c-b621-4b2fa15e0208'

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
    print r.json()
    if r.status_code in HTTP_STATUS_CODES:
        print HTTP_STATUS_CODES[r.status_code]
    else:
        return r.json()

@sleep_and_retry
@limits(calls=1, period = 2)
def getMatchById(matchId):
    escapedMatchId = matchId
    url = 'https://euw1.api.riotgames.com/lol/match/v4/matches/%s?api_key=%s' % (escapedMatchId, api_key)
    r = requests.get(url)
    if r.status_code in HTTP_STATUS_CODES:
        print HTTP_STATUS_CODES[r.status_code]
    else:
        return r.json()

@sleep_and_retry
@limits(calls=1, period = 2)
def getMatchlistsBySummonerId(summonerId):
    escapedSummonerId = urllib.quote(summonerId.encode('utf -8'))
    url = 'https://euw1.api.riotgames.com/lol/match/v4/matchlists/by-account/%s?api_key=%s' % (escapedSummonerId, api_key)
    r = requests.get(url)
    if r.status_code in HTTP_STATUS_CODES:
        print HTTP_STATUS_CODES[r.status_code]
    else:
        return r.json()

@sleep_and_retry
@limits(calls=1, period = 2)
def getSummonerBySummonerName(summonerName):
    escapedSummonerName = urllib.quote(summonerName.encode('utf -8'))
    url = 'https://euw1.api.riotgames.com/lol/summoner/v4/summoners/by-name/%s?api_key=%s' % (escapedSummonerName, api_key)
    r = requests.get(url)
    if r.status_code in HTTP_STATUS_CODES:
        print HTTP_STATUS_CODES[r.status_code]
    else:
        return r.json()
