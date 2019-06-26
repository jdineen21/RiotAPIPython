
from sqlalchemy import create_engine
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Boolean
from sqlalchemy import ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

engine = create_engine('sqlite:///sqlite/main.db')

class Match(Base):

    __tablename__ = 'matches'

    gameCreation = Column(Integer)
    gameDuration = Column(Integer)
    gameId = Column(Integer, primary_key=True)
    gameMode = Column(String)
    gameType = Column(String)
    gameVersion = Column(String)
    mapId = Column(Integer)

    platformId = Column(String)
    queueId = Column(Integer)
    seasonId = Column(Integer)

    participants = relationship('Participant', back_populates='match')
    teams = relationship('Team', back_populates='match')

class Participant(Base):

    __tablename__ = 'participants'

    id = Column(Integer, primary_key=True)
    gameId = Column(Integer, ForeignKey('matches.gameId'))
    championId = Column(Integer)
    highestAchievedSeasonTier = Column(String)
    accountId = Column(String, ForeignKey('players.accountId'))
    spell1Id = Column(Integer)
    spell2Id = Column(Integer)
    teamId = Column(Integer)

    match = relationship('Match', back_populates='participants')
    players = relationship('Player', back_populates='particpant')

    stats = relationship('Stats', back_populates='participant')

class Player(Base):

    __tablename__ = 'players'

    accountId = Column(String, primary_key=True)
    currentAccountId = Column(String)
    currentPlatformId = Column(String)
    matchHistoryUri = Column(String)
    platformId = Column(String)
    profileIcon = Column(Integer)
    summonerId = Column(String)
    summonerName = Column(String)

    particpant = relationship("Participant", back_populates="players")

class Stats(Base):

    __tablename__ = 'stats'

    id = Column(Integer, primary_key=True)
    participantId = Column(Integer, ForeignKey('participants.id'))
    assists = Column(Integer)
    champLevel = Column(Integer)
    combatPlayerScore = Column(Integer)
    damageDealtToObjectives = Column(Integer)
    damageDealtToTurrets = Column(Integer)
    damageSelfMitigated = Column(Integer)
    deaths = Column(Integer)
    doubleKills = Column(Integer)
    firstBloodAssist = Column(Boolean)
    firstBloodKill = Column(Boolean)
    firstInhibitorAssist = Column(Boolean)
    firstInhibitorKill = Column(Boolean)
    firstTowerAssist = Column(Boolean)
    firstTowerKill = Column(Boolean)
    goldEarned = Column(Integer)
    goldSpent = Column(Integer)
    inhibitorKills = Column(Integer)
    item0 = Column(Integer)
    item1 = Column(Integer)
    item2 = Column(Integer)
    item3 = Column(Integer)
    item4 = Column(Integer)
    item5 = Column(Integer)
    item6 = Column(Integer)
    killingSprees = Column(Integer)
    kills = Column(Integer)
    largestCriticalStrike = Column(Integer)
    largestKillingSpree = Column(Integer)
    largestMultiKill = Column(Integer)
    longestTimeSpentLiving = Column(Integer)
    magicDamageDealt = Column(Integer)
    magicDamageDealtToChampions = Column(Integer)
    magicalDamageTaken = Column(Integer)
    neutralMinionsKilled = Column(Integer)
    objectivePlayerScore = Column(Integer)
    pentaKills = Column(Integer)
    perk0 = Column(Integer)
    perk0Var1 = Column(Integer)
    perk0Var2 = Column(Integer)
    perk0Var3 = Column(Integer)
    perk1 = Column(Integer)
    perk1Var1 = Column(Integer)
    perk1Var2 = Column(Integer)
    perk1Var3 = Column(Integer)
    perk2 = Column(Integer)
    perk2Var1 = Column(Integer)
    perk2Var2 = Column(Integer)
    perk2Var3 = Column(Integer)
    perk3 = Column(Integer)
    perk3Var1 = Column(Integer)
    perk3Var2 = Column(Integer)
    perk3Var3 = Column(Integer)
    perk4 = Column(Integer)
    perk4Var1 = Column(Integer)
    perk4Var2 = Column(Integer)
    perk4Var3 = Column(Integer)
    perk5 = Column(Integer)
    perk5Var1 = Column(Integer)
    perk5Var2 = Column(Integer)
    perk5Var3 = Column(Integer)
    perkPrimaryStyle = Column(Integer)
    perkSubStyle = Column(Integer)
    physicalDamageDealt = Column(Integer)
    physicalDamageDealtToChampions = Column(Integer)
    physicalDamageTaken = Column(Integer)
    playerScore0 = Column(Integer)
    playerScore1 = Column(Integer)
    playerScore2 = Column(Integer)
    playerScore3 = Column(Integer)
    playerScore4 = Column(Integer)
    playerScore5 = Column(Integer)
    playerScore6 = Column(Integer)
    playerScore7 = Column(Integer)
    playerScore8 = Column(Integer)
    playerScore9 = Column(Integer)
    quadraKills = Column(Integer)
    sightWardsBoughtInGame = Column(Integer)
    statPerk0 = Column(Integer)
    statPerk1 = Column(Integer)
    statPerk2 = Column(Integer)
    timeCCingOthers = Column(Integer)
    totalDamageDealt = Column(Integer)
    totalDamageDealtToChampions = Column(Integer)
    totalDamageTaken = Column(Integer)
    totalHeal = Column(Integer)
    totalMinionsKilled = Column(Integer)
    totalPlayerScore = Column(Integer)
    totalScoreRank = Column(Integer)
    totalTimeCrowdControlDealt = Column(Integer)
    totalUnitsHealed = Column(Integer)
    tripleKills = Column(Integer)
    trueDamageDealt = Column(Integer)
    trueDamageDealtToChampions = Column(Integer)
    trueDamageTaken = Column(Integer)
    turretKills = Column(Integer)
    unrealKills = Column(Integer)
    visionScore = Column(Integer)
    visionWardsBoughtInGame = Column(Integer)
    win = Column(Boolean)

    participant = relationship('Participant', back_populates='stats')

class Team(Base):

    __tablename__ = 'teams'

    id = Column(Integer, primary_key=True)
    gameId = Column(Integer, ForeignKey('matches.gameId'))
    baronKills = Column(Integer)
    dominionVictoryScore = Column(Integer)
    dragonKills = Column(Integer)
    firstBaron = Column(Boolean)
    firstBlood = Column(Boolean)
    firstDragon = Column(Boolean)
    firstInhibitor = Column(Boolean)
    firstRiftHerald = Column(Boolean)
    firstTower = Column(Boolean)
    inhibitorKills = Column(Integer)
    riftHeraldKills = Column(Integer)
    teamId = Column(Integer)
    towerKills = Column(Integer)
    vilemawKills = Column(Integer)
    win = Column(String)

    match = relationship('Match', back_populates='teams')
    bans = relationship('Ban', back_populates='team')

class Ban(Base):

    __tablename__ = 'bans'

    bansId = Column(Integer, primary_key=True)
    teamId = Column(Integer, ForeignKey('teams.id'))
    pickTurn = Column(Integer)
    championId = Column(Integer)

    team = relationship('Team', back_populates='bans')

Base.metadata.create_all(bind=engine)