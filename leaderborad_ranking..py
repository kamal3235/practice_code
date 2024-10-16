


ranked = [100, 90, 90, 80]
player = [70, 80, 105]

ranks = []
ranked = sorted(set(ranked), reverse=True)
n = len(ranked)
for score in player:
    while n>0 and score>= ranked[n-1]:
        n -= 1
    ranks.append(n+1)
print(ranks)


def climbingLeaderboard(ranked, player):
    ranks = [] # Create an empty list to store player's ranks
    ranked = sorted(set(ranked), reverse=True) # Sort the ranked list in descending order and remove duplicates
    l = len(ranked) # Initialize a variable l to the length of the ranked list
    for score in player: # Loop through each score in the player list
        while (l > 0) and (score >= ranked[l-1]): # Check if the score is greater than or equal to the current score in ranked list
            l -= 1 # If it is, decrement l to move to the next score in ranked list
        ranks.append(l+1) # Add the player's rank to the ranks list
    return ranks # Return the list of ranks
