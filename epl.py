import random

teams = ['arsenal',
         'aston villa',
         'bournemouth',
         'brighton',
         'burnley',
         'chelsea',
         'crystal palace',
         'everton',
         'Leicester',
         'Man city',
         'Liverpool',
         'Man united',
         'newcastle',
         'norwich',
         'sheffield',
         'southampton',
         'tottenham',
         'watford',
         'west ham',
         'wolves']

opponents = teams

for i in range(len(teams)):
    for j in range(len(opponents)):
        # teams cannot have themselves as opponents
        if teams[i] != opponents[j]:
            print(teams[i] + " " + str(random.randint(0, 9)) + " vs " + str(random.randint(0, 9)) + " " + opponents[j])
