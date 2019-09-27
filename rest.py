
from flask import Flask, request
from flask_restful import Resource, Api
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

from dotenv import load_dotenv

import json
import requests
import urllib
import os

load_dotenv()

api_key = os.getenv('RIOT_API_KEY')

app = Flask(__name__)
api = Api(app)

limiter = Limiter(
    app,
    key_func=get_remote_address,
    default_limits=["20/second", "100/2minute"]
)

class FeaturedGames(Resource):
    def get(self):
        r = requests.get('https://euw1.api.riotgames.com/lol/spectator/v4/featured-games?api_key=%s' % (api_key))
        return r.json(), r.status_code

class Match(Resource):
    def get(self, matchId):
        r = requests.get('https://euw1.api.riotgames.com/lol/match/v4/matches/%s?api_key=%s' % (matchId, api_key))
        return r.json(), r.status_code

class Timeline(Resource):
    def get(self, matchId):
        r = requests.get('https://euw1.api.riotgames.com//lol/match/v4/timelines/by-match/%s?api_key=%s' % (matchId, api_key))
        return r.json(), r.status_code

class Matchlists(Resource):
    def get(self, summonerId):
        r = requests.get('https://euw1.api.riotgames.com/lol/match/v4/matchlists/by-account/%s?api_key=%s' % (summonerId, api_key))
        return r.json(), r.status_code

class Summoner(Resource):
    def get(self, summonerName):
        escapedSummonerName = urllib.quote(summonerName.encode('utf-8'))
        r = requests.get('https://euw1.api.riotgames.com/lol/summoner/v4/summoners/by-name/%s?api_key=%s' % (escapedSummonerName, api_key))
        return r.json(), r.status_code

api.add_resource(FeaturedGames, '/featured-games')
api.add_resource(Match, '/match/<matchId>')
api.add_resource(Timeline, '/timeline/<matchId>')
api.add_resource(Matchlists, '/matchlists/<summonerId>')
api.add_resource(Summoner, '/summoner/<summonerName>')


if __name__ == '__main__':
     app.run(port='5002')
