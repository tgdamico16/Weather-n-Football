from ohmysportsfeedspy import MySportsFeeds
import json

msf = MySportsFeeds(version ="1.2")
msf.authenticate("05e421a4-2932-44c1-99e4-0fb8e2", "mysportsfeeds100")
output = msf.msf_get_data(league='nfl',season='2018-2019-regular',
    feed='cumulative_player_stats',format='json',team='dallas-cowboys')

with open("E:/school/2018-19/caps/A Foot in the Door/pythonFiles/results/boys.json","w+") as f:
    json.dump(output, f)