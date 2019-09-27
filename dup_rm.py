
meta_file = open('match-data.meta', 'a+')
match_file = open('match-seed.data', 'a+')
match_timeline_file = open('match-timeline-seed.data', 'a+')

meta_file_list = meta_file.read().split('\n')
match_file_list = match_file.read().split('\n')
match_timeline_list = match_timeline_file.read().split('\n')

print len(meta_file_list)
print len(list( dict.fromkeys(meta_file_list) ))

print len(match_file_list)
print len(list( dict.fromkeys(match_file_list) ))

print len(match_timeline_list)
print len(list( dict.fromkeys(match_timeline_list) ))