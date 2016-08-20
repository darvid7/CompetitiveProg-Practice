"""
@author: David Lei
@since: 13/08/2016
@modified: 

"""

wins = {

}
for i in range(16):
    data = input().split(' ')
    team1_name = data[0]
    team2_name = data[1]
    team1_score = data[2]
    team2_score = data[3]

    if team1_score > team2_score: # team 1 wins
        winning_team = team1_name
    else:
        # team 2 wins, as no draw
        winning_team = team2_name

    try:
        wins[winning_team] = wins[winning_team] + 1
    except KeyError:
        wins[winning_team] = 1

max_wins = 0
max_wins_team = ''
for team in wins:
    if wins[team] > max_wins:
        max_wins_team = team
        max_wins = wins[team]
print(max_wins_team)
