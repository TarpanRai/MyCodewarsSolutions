# Your team is in a football game.
# If they win they gain 3 points
# If they lose they gain 0 points
# If they tie they get 1 point
# Given an array of match score, find the amount of points gained

def points(games):
    # Variable to store points
    points = 0
    for i in games:
        # Split the scores into x and y variable
        x, y = i.split(":")
        # If win add 3
        if x > y:
            points += 3
        # If tie add 1
        elif x == y:
            points += 1
        # No need for lose cause no points gained
    return points

