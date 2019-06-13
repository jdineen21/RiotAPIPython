
import urllib
import json
import time
import csv

print int(time.time())

last = None
rate_limit = '''{
    "status": {
        "message": "Rate limit exceeded", 
        "status_code": 429
    }
}'''



while True:

    request = urllib.urlopen('https://euw1.api.riotgames.com/lol/spectator/v4/featured-games?api_key=RGAPI-dd53ee61-5ade-444b-87c4-028dafb48b1e')
    raw_json = request.read()
    parsed = json.loads(raw_json)
    pretty_json = json.dumps(parsed, indent=4, sort_keys=True)

    if not pretty_json == last:
        if not pretty_json == rate_limit:
            print int(time.time())
            file_name = 'game-%s.json' % str(int(time.time()))
            with open(file_name, 'w') as json_file:
                json_file.write(pretty_json)
            last = pretty_json
        else:
            time.sleep(120)

    time.sleep(1.5)


