
from importer.match import Match
from importer.match import Player
from importer.match import Participant
from importer.match import Stats
from importer.match import Team
from importer.match import Ban

from sqlalchemy import exists

import json

def insertData(session, matchData):
    row = Match(
        gameCreation=matchData.get('gameCreation'),
        gameDuration=matchData.get('gameDuration'), 
        gameId=matchData.get('gameId'), 
        gameMode=matchData.get('gameMode'), 
        gameType=matchData.get('gameType'),
        gameVersion=matchData.get('gameVersion'),
        mapId=matchData.get('mapId'),
        platformId=matchData.get('platformId'),
        queueId=matchData.get('queueId'),
        seasonId=matchData.get('seasonId')
    )

    row.participants = []
    for x in range(len(matchData['participants'])):

        participantData = matchData['participants'][x]
        playerData = matchData['participantIdentities'][x]['player']
        stats = matchData['participants'][x]['stats']

        part = Participant(
            championId=participantData.get('championId'),
            highestAchievedSeasonTier=participantData.get('highestAchievedSeasonTier'),
            spell1Id=participantData.get('spell1Id'),
            spell2Id=participantData.get('spell2Id'),
            teamId=participantData.get('teamId')
        )
        

        if not session.query(exists().where(Player.accountId==playerData.get('accountId'))).scalar():
            part.players = Player(
                accountId = playerData.get('accountId'),
                currentAccountId = playerData.get('currentAccountId'),
                currentPlatformId = playerData.get('currentPlatformId'),
                matchHistoryUri = playerData.get('matchHistoryUri'),
                platformId = playerData.get('platformId'),
                profileIcon = playerData.get('profileIcon'),
                summonerId = playerData.get('summonerId'),
                summonerName = playerData.get('summonerName')
            )
        else:
            part = Participant(
                championId=participantData.get('championId'),
                highestAchievedSeasonTier=participantData.get('highestAchievedSeasonTier'),
                accountId=playerData.get('accountId'),
                spell1Id=participantData.get('spell1Id'),
                spell2Id=participantData.get('spell2Id'),
                teamId=participantData.get('teamId')
            )
        row.participants.append(part)

        part.stats = []
        s = Stats(
            assists = stats.get('assists'),
            champLevel = stats.get('champLevel'),
            combatPlayerScore = stats.get('combatPlayerScore'),
            damageDealtToObjectives = stats.get('damageDealtToObjectives'),
            damageDealtToTurrets = stats.get('damageDealtToTurrets'),
            damageSelfMitigated = stats.get('damageSelfMitigated'),
            deaths = stats.get('deaths'),
            doubleKills = stats.get('doubleKills'),
            firstBloodAssist = stats.get('firstBloodAssist'),
            firstBloodKill = stats.get('firstBloodKill'),
            firstInhibitorAssist = stats.get('firstInhibitorAssist'),
            firstInhibitorKill = stats.get('firstInhibitorKill'),
            firstTowerAssist = stats.get('firstTowerAssist'),
            firstTowerKill = stats.get('firstTowerKill'),
            goldEarned = stats.get('goldEarned'),
            goldSpent = stats.get('goldSpent'),
            inhibitorKills = stats.get('inhibitorKills'),
            item0 = stats.get('item0'),
            item1 = stats.get('item1'),
            item2 = stats.get('item2'),
            item3 = stats.get('item3'),
            item4 = stats.get('item4'),
            item5 = stats.get('item5'),
            item6 = stats.get('item6'),
            killingSprees = stats.get('killingSprees'),
            kills = stats.get('kills'),
            largestCriticalStrike = stats.get('largestCriticalStrike'),
            largestKillingSpree = stats.get('largestKillingSpree'),
            largestMultiKill = stats.get('largestMultiKill'),
            longestTimeSpentLiving = stats.get('longestTimeSpentLiving'),
            magicDamageDealt = stats.get('magicDamageDealt'),
            magicDamageDealtToChampions = stats.get('magicDamageDealtToChampions'),
            magicalDamageTaken = stats.get('magicalDamageTaken'),
            neutralMinionsKilled = stats.get('neutralMinionsKilled'),
            objectivePlayerScore = stats.get('objectivePlayerScore'),
            participantId = stats.get('participantId'),
            pentaKills = stats.get('pentaKills'),
            perk0 = stats.get('perk0'),
            perk0Var1 = stats.get('perk0Var1'),
            perk0Var2 = stats.get('perk0Var2'),
            perk0Var3 = stats.get('perk0Var3'),
            perk1 = stats.get('perk1'),
            perk1Var1 = stats.get('perk1Var1'),
            perk1Var2 = stats.get('perk1Var2'),
            perk1Var3 = stats.get('perk1Var3'),
            perk2 = stats.get('perk2'),
            perk2Var1 = stats.get('perk2Var1'),
            perk2Var2 = stats.get('perk2Var2'),
            perk2Var3 = stats.get('perk2Var3'),
            perk3 = stats.get('perk3'),
            perk3Var1 = stats.get('perk3Var1'),
            perk3Var2 = stats.get('perk3Var2'),
            perk3Var3 = stats.get('perk3Var3'),
            perk4 = stats.get('perk4'),
            perk4Var1 = stats.get('perk4Var1'),
            perk4Var2 = stats.get('perk4Var2'),
            perk4Var3 = stats.get('perk4Var3'),
            perk5 = stats.get('perk5'),
            perk5Var1 = stats.get('perk5Var1'),
            perk5Var2 = stats.get('perk5Var2'),
            perk5Var3 = stats.get('perk5Var3'),
            perkPrimaryStyle = stats.get('perkPrimaryStyle'),
            perkSubStyle = stats.get('perkSubStyle'),
            physicalDamageDealt = stats.get('physicalDamageDealt'),
            physicalDamageDealtToChampions = stats.get('physicalDamageDealtToChampions'),
            physicalDamageTaken = stats.get('physicalDamageTaken'),
            playerScore0 = stats.get('playerScore0'),
            playerScore1 = stats.get('playerScore1'),
            playerScore2 = stats.get('playerScore2'),
            playerScore3 = stats.get('playerScore3'),
            playerScore4 = stats.get('playerScore4'),
            playerScore5 = stats.get('playerScore5'),
            playerScore6 = stats.get('playerScore6'),
            playerScore7 = stats.get('playerScore7'),
            playerScore8 = stats.get('playerScore8'),
            playerScore9 = stats.get('playerScore9'),
            quadraKills = stats.get('quadraKills'),
            sightWardsBoughtInGame = stats.get('sightWardsBoughtInGame'),
            statPerk0 = stats.get('statPerk0'),
            statPerk1 = stats.get('statPerk1'),
            statPerk2 = stats.get('statPerk2'),
            timeCCingOthers = stats.get('timeCCingOthers'),
            totalDamageDealt = stats.get('totalDamageDealt'),
            totalDamageDealtToChampions = stats.get('totalDamageDealtToChampions'),
            totalDamageTaken = stats.get('totalDamageTaken'),
            totalHeal = stats.get('totalHeal'),
            totalMinionsKilled = stats.get('totalMinionsKilled'),
            totalPlayerScore = stats.get('totalPlayerScore'),
            win = stats.get('win')
        )
        part.stats.append(s)

    row.teams = []
    for x in range(len(matchData.get('teams'))):
        teamData = matchData.get('teams')[x]
        t = Team(
            baronKills = teamData.get('baronKills'),
            dominionVictoryScore = teamData.get('dominionVictoryScore'),
            dragonKills = teamData.get('dragonKills'),
            firstBaron = teamData.get('firstBaron'),
            firstBlood = teamData.get('firstBlood'),
            firstDragon = teamData.get('firstDragon'),
            firstInhibitor = teamData.get('firstInhibitor'),
            firstRiftHerald = teamData.get('firstRiftHerald'),
            firstTower = teamData.get('firstTower'),
            inhibitorKills = teamData.get('inhibitorKills'),
            riftHeraldKills = teamData.get('riftHeraldKills'),
            teamId = teamData.get('teamId'),
            towerKills = teamData.get('towerKills'),
            vilemawKills = teamData.get('vilemawKills'),
            win = teamData.get('win')
        )
        row.teams.append(t)

        t.bans = []

        banData = matchData.get('teams')[x]['bans']
        for y in range(len(banData)):
            b = Ban(
                pickTurn = banData[y]['pickTurn'],
                championId = banData[y]['championId']
            )
            t.bans.append(b)
    return row