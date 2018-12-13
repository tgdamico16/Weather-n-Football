from ohmysportsfeedspy import MySportsFeeds
import json
import requests
import urllib.request

def msf(season, feed, team):
    # f = open(('E:/school/2018-19/caps/A Foot in the Door/json/%(feed)s-nfl-%(season)s.json' %
    #             {'feed': feed, 'season': season}), 'w+')
    msf = MySportsFeeds(version ='1.2')
    msf.authenticate('API_KEY', 'PASSWORD')

    output = msf.msf_get_data(force = 'true', league='nfl', feed = feed, season=season, 
                                format='json', team = team)
        #, position = 'te'
    # f.write(output)
    # json.dump(output, f)
    return output

def weather(state,city):
    url = ('http://api.wunderground.com/api/API_KEY/forecast10day/q/%(state)s/%(city)s.json' %
                {'state': state, 'city': city})
    jsonData = json.loads(urllib.request.urlopen(url).read())

    # with open('E:/school/2018-19/caps/A Foot in the Door/json/ny.json', 'w+') as f:
    #     json.dump(jsonData, f)

    return jsonData

# msf('2018-2019-regular','full_game_schedule', 'kansascity-chiefs')
# weather('NY', 'New_York')
