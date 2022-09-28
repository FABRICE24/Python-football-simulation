from random import randint

teams_with_strengths = [
    {'arsenal': 5},
    {'aston villa': 2},
    {'bournemouth': 3},
    {'brighton': 3},
    {'burnley': 2},
    {'chelsea': 5},
    {'crystal palace': 2},
    {'everton': 3},
    {'leicester': 4},
    {'liverpool': 5},
    {'man city': 5},
    {'man united': 5},
    {'newcastle': 3},
    {'norwich': 2},
    {'sheffield': 3},
    {'southampton': 3},
    {'tottenham': 5},
    {'watford': 3},
    {'west ham': 2},
    {'wolves': 4}
]

opponents = teams_with_strengths

for i in range(len(teams_with_strengths)):
    for j in range(len(opponents)):
            for team in teams_with_strengths[i]:
                for team_b in opponents[j]:
                    # teams cannot have themselves as opponents
                    if team != team_b:
                        print(team + " " + str(randint(0, 9)) + " vs " + str(randint(0, 9)) + " " + team_b)

# TODO: generate randomness depending on strength of teams
#WHAT DO YOU BASE ON?