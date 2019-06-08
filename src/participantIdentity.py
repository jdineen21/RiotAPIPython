
from player import *

class ParticipantIdentity:
    def __init__(self, identitiy):
        self.participantId = identitiy['participantId']
        self.player = Player(identitiy['player'])
