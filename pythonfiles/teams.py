
def teamDict():
    team = {'Arizona Cardinals', 'Atlanta Falcons', 'Baltimore Ravens', 'Buffalo Bills', 'Carolina Panthers', 'Chicago Bears',
            'Cincinnati Bengals', 'Cleveland Browns', 'Dallas Cowboys', 'Denver Broncos', 'Detroit Lions', 'Green Bay Packers',
            'Houston Texans', 'Indianapolis Colts', 'Jacksonville Jaguars', 'Kansas City Chiefs', 'Los Angeles Chargers', 'Los Angeles Rams',
            'Miami Dolphins', 'Minnesota Vikings', 'New England Patriots', 'New Orleans Saints', 'New York Giants',
            'New York Jets', 'Oakland Raiders', 'Philadelphia Eagles', 'Pittsburgh Steelers', 'San Francisco 49ers', 'Seattle Seahawks',
            'Tampa Bay Buccaneers', 'Tennessee Titans', 'Washington Redskins'}
    return team

def teamCity(team):
    location = [['Phoenix', 'Atlanta', 'Baltimore', 'Buffalo', 'Charlotte', 'Chicago', 'Cincinnati', 'Cleveland', 'Dallas', 'Denver', 'Detroit', 'Green_Bay',
            'Houston', 'Indianapolis', 'Jacksonville', 'Kansas_City', 'Los_Angeles', 'Los_Angeles', 'Miami', 'Minneapolis', 'Boston', 'New_Orleans', 'New_York',
            'New_York', 'Oakland', 'Philadelphia', 'Pittsburgh', 'San_Francisco', 'Seattle', 'Tampa_Bay', 'Nashville', 'Washington'], ['AZ', 'GA', 'MD', 'NY',
            'NC', 'IL', 'OH', 'OH', 'TX', 'CO', 'MI', 'WI', 'TX', 'IN', 'FL', 'MO', 'CA', 'CA', 'FL', 'MN', 'MA', 'LA', 'NY', 'NY', 'CA', 'PA', 'PA', 'CA', 'WA',
            'FL', 'TN', 'DC']]

    if (team == 'Arizona Cardinals'):
        return location[1][0], location[0][0]
    elif (team == 'Atlanta Falcons'):
        return location[1][1], location[0][1]
    elif (team == 'Baltimore Ravens'):
        return location[1][2], location[0][2]
    elif (team == 'Buffalo Bills'):
        return location[1][3], location[0][3]
    elif (team == 'Carolina Panthers'):
        return location[1][4], location[0][4]
    elif (team == 'Chicago Bears'):
        return location[1][5], location[0][5]
    elif (team == 'Cincinnati Bengals'):
        return location[1][6], location[0][6]
    elif (team == 'Cleveland Browns'):
        return location[1][7], location[0][7]
    elif (team == 'Dallas Cowboys'):
        return location[1][8], location[0][8]
    elif (team == 'Denver Broncos'):
        return location[1][9], location[0][9]
    elif (team == 'Detroit Lions'):
        return location[1][10], location[0][10]
    elif (team == 'Green Bay Packers'):
        return location[1][11], location[0][11]
    elif (team == 'Houston Texans'):
        return location[1][12], location[0][12]
    elif (team == 'Indianapolis Colts'):
        return location[1][13], location[0][13]
    elif (team == 'Jacksonville Jaguars'):
        return location[1][14], location[0][14]
    elif (team == 'Kansas City Chiefs'):
        return location[1][15], location[0][15]
    elif (team == 'Los Angeles Chargers'):
        return location[1][16], location[0][16]
    elif (team == 'Los Angeles Rams'):
        return location[1][17], location[0][17]
    elif (team == 'Miami Dolphins'):
        return location[1][18], location[0][18]
    elif (team == 'Minnesota Vikings'):
        return location[1][19], location[0][19]
    elif (team == 'New England Patriots'):
        return location[1][20], location[0][20]
    elif (team == 'New Orleans Saints'):
        return location[1][21], location[0][21]
    elif (team == 'New York Giants'):
        return location[1][22], location[0][22]
    elif (team == 'New York Jets'):
        return location[1][23], location[0][23]
    elif (team == 'Oakland Raiders'):
        return location[1][24], location[0][24]
    elif (team == 'Philadelphia Eagles'):
        return location[1][25], location[0][25]
    elif (team == 'Pittsburgh Steelers'):
        return location[1][26], location[0][26]
    elif (team == 'San Francisco 49ers'):
        return location[1][27], location[0][27]
    elif (team == 'Seattle Seahawks'):
        return location[1][28], location[0][28]
    elif (team == 'Tampa Bay Buccaneers'):
        return location[1][29], location[0][29]
    elif (team == 'Tennessee Titans'):
        return location[1][30], location[0][30]
    else:
        return location[1][31], location[0][31]

def indoor():
    teams = ('Dallas Cowboys', 'Indianapolis Colts', 'Atlanta Falcons', 'Houston Texans', 'Arizona Cardinals',
                'Detroit Lions', 'New Orleans Saints', 'Minnesota Vikings')
    return teams
# teamCity()