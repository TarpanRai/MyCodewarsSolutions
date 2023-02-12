# Imagine a grid.
# You take 1 minutes to travel a single block.
# You can travel North/South/East/West
# Given an array with random directions. Find if that array will
# return you to the starting point in time

def is_valid_walk(walk):
    # False if the length of the array is more than 10 since
    # it would mean that it takes longer than 10 minutes
    if len(walk) != 10:
        return False

    # X-axis for North and South and Y-axis for East and West
    # (X,Y)
    x = 0
    y = 0

    # When you travel north --> + 1 on X
    # When you travel south --> - 1 on X
    # When you travel east  --> + 1 on Y
    # When you travel west  --> - 1 on Y
    for i in range(len(walk)):
        if walk[i] == 'n':
            x += 1
        elif walk[i] == 's':
            x -= 1
        elif walk[i] == 'e':
            y += 1
        elif walk[i] == 'w':
            y -= 1

    # Check if we are at the starting position of (0,0)
    if x == 0 and y == 0:
        return True
    else:
        return False