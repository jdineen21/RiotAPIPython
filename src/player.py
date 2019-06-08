class Player:
    def __init__(self, player):
        self.accountId = player['accountId']
        self.currentAccountId = player['currentAccountId']
        self.currentPlatformId = player['currentPlatformId']
        self.matchHistoryUri = player['matchHistoryUri']
        self.platformId = player['platformId']
        self.profileIcon = player['profileIcon']
        self.summonerId = player['summonerId']
        self.summonerName = player['summonerName']