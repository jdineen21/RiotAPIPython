import api

meta_file = open('match-data.meta', 'a+')
match_file = open('match-seed.data', 'a+')
match_timeline_file = open('match-timeline-seed.data', 'a+')

while True:

    featuredGames = api.handler.getFeaturedGames()

    for x in range(len(featuredGames['gameList'])):

        for y in range(len(featuredGames['gameList'][x]['participants'])):

            summonerName = featuredGames['gameList'][x]['participants'][y]['summonerName']
            print summonerName
            summonerId = api.handler.getSummonerBySummonerName(summonerName)['accountId']
            print summonerId
            matchlists = api.handler.getMatchlistsBySummonerId(summonerId)['matches']

            for z in range(len(matchlists)):

                matchData = api.handler.getMatchById(matchlists[z]['gameId'])
                
                if matchData is None:
                    print 'Skipping Nonetype Data'
                elif not '9.18' in matchData.get('gameVersion'):
                    print 'Skipping Outdated Data'
                elif matchlists[z]['gameId'] in meta_file.read().split('\n'):
                    print 'Skipping Overlapping Data'
                else:
                    print 'Data Inserted'
                    meta_file.write(str(matchlists[z]['gameId'])+'\n')
                    match_file.write(str(matchData)+'\n')
                    match_timeline_file.write(str(api.handler.getMatchTimelineById(matchlists[z]['gameId']))+'\n')