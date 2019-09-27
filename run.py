
import api
import datetime

meta_file = open('match-data.meta', 'a+')
match_file = open('match-seed.data', 'a+')
match_timeline_file = open('match-timeline-seed.data', 'a+')

while True:

    featuredGames = api.getFeaturedGames()

    for x in range(len(featuredGames['gameList'])):

        for y in range(len(featuredGames['gameList'][x]['participants'])):

            summonerName = featuredGames['gameList'][x]['participants'][y]['summonerName']
            print summonerName
            summonerId = api.getSummonerBySummonerName(summonerName)['accountId']
            print summonerId
            matchlists = api.getMatchlistsBySummonerId(summonerId)['matches']

            # Remove matches not in between two dates
            # Cuts down on unneccesary api calls
            matchlistsBackup = list(matchlists)
            startDate = int(datetime.datetime(2019, 9, 12).strftime('%s'))*1000
            endDate = int(datetime.datetime(2019, 9, 26).strftime('%s'))*1000
            deleteCount = 0

            for i in range(len(matchlistsBackup)):
                if not startDate < matchlistsBackup[i]['timestamp'] < endDate:
                    deleteCount += 1
                    matchlists.remove(matchlistsBackup[i])

            # Remove incorrect queue type matches
            matchlistsBackup = list(matchlists)
            for i in range(len(matchlistsBackup)):
                if not matchlistsBackup[i]['queue'] in [400, 420, 430, 440, 450]:
                    deleteCount += 1
                    matchlists.remove(matchlistsBackup[i])
            
            print 'Deleted %s matches from matchlist' % (deleteCount)

            for z in range(len(matchlists)):

                matchData = api.getMatchById(matchlists[z]['gameId'])
                timelineData = api.getMatchTimelineById(matchlists[z]['gameId'])
                
                if matchData is None:
                    print 'Skipping Nonetype Data'
                elif timelineData is None:
                    print 'Skipping Nonetype Data'
                elif not '9.18' in matchData.get('gameVersion'):
                    print 'Skipping Incorrect Game Version'
                elif not matchData.get('queueId') in [400, 420, 430, 440, 450]:
                    print 'Skipping Incorrect Queue Type'
                elif str(matchData.get('gameId')) in meta_file.read().split('\n'):
                    print 'Skipping Overlapping Data'
                else:
                    print 'Data Inserted'
                    meta_file.write(str(matchData.get('gameId'))+'\n')
                    match_file.write(str(matchData)+'\n')
                    match_timeline_file.write(str(timelineData)+'\n')