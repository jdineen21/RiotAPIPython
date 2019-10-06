
import api
import json
import datetime

meta_file = open('match-data.meta', 'a+')
match_file = open('match-seed.data', 'a+')
match_timeline_file = open('match-timeline-seed.data', 'a+')

meta_file.close()
match_file.close()
match_timeline_file.close()

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
            # Cuts down on unneccesary api calls
            matchlistsBackup = list(matchlists)
            for i in range(len(matchlistsBackup)):
                if not matchlistsBackup[i]['queue'] in [400, 420, 430, 440, 450]:
                    deleteCount += 1
                    matchlists.remove(matchlistsBackup[i])

            # Remove overlapping match data pre call
            # Cuts down on unneccesary api calls
            with open('match-data.meta', 'r+') as meta_file_read:
                meta_file_list = meta_file_read.read().split('\n')
            
            matchlistsBackup = list(matchlists)
            for i in range(len(matchlistsBackup)):
                if str(matchlistsBackup[i]['gameId']) in meta_file_list:
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
                else:
                    print 'Data Inserted'
                    meta_file = open('match-data.meta', 'a+')
                    match_file = open('match-seed.data', 'a+')
                    match_timeline_file = open('match-timeline-seed.data', 'a+')

                    meta_file.write(str(matchData.get('gameId'))+'\n')
                    match_file.write(json.dumps(matchData)+'\n')
                    match_timeline_file.write(json.dumps(timelineData)+'\n')

                    meta_file.close()
                    match_file.close()
                    match_timeline_file.close()