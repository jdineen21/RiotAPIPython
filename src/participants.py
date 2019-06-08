
from stats import *

class Participants:
     def __init__(self, participant):
         self.championId = participant['championId']
         # Throws error dont know why
         #self.highestAchievedSeasonTier = participant['highestAchievedSeasonTier']
         self.participantId = participant['participantId']
         self.spell1Id = participant['spell1Id']
         self.spell2Id = participant['spell2Id']
         self.stats = Stats(participant['stats'])
         self.teamId = participant['teamId']

        # Timeline data goes here
        # Need its own class?
        # self.timeline = Timeline()