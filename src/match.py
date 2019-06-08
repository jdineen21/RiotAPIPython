
from participantIdentity import ParticipantIdentity
from participants import Participants
from teams import Teams

import riotApiHandler

class Match:
    def __init__(self, matchData):
        self.gameCreation = matchData['gameCreation']
        self.gameDuration = matchData['gameDuration']
        self.gameId = matchData['gameId']
        self.gameMode = matchData['gameMode']
        self.gameType = matchData['gameType']
        self.gameVersion = matchData['gameVersion']
        self.mapId = matchData['mapId']

        self.participantIdentities = []
        for x in range(len(matchData['participantIdentities'])):
            participantIdentity = ParticipantIdentity(matchData['participantIdentities'][x])
            self.participantIdentities.append(participantIdentity)

        self.participants = []
        for x in range(len(matchData['participants'])):
            participant = Participants(matchData['participants'][x])
            self.participants.append(participant)

        self.platformId = matchData['platformId']
        self.queueId = matchData['queueId']
        self.seasonId = matchData['seasonId']

        self.teams = []
        for x in range(len(matchData['teams'])):
            team = matchData['teams'][x]
            self.teams.append(Teams(team))