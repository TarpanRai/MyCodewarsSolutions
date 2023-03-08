# A man is standing at a point. He can move in any cardinal directions ("NORTH", "SOUTH", "WEST", "EAST").
# He has to go past a desert and has been given a paper with a list of directions to follow to get out of the desert.
# He realised that the person who gave him this paper had made some mistakes.
# Some directions given leads to the same place he was just a few moments ago.
# For example ["NORTH","SOUTH"] which is useless.
# Write a function that removes this useless directions that lead to nowhere

def dirReduc(arr):
    # Create a dictionary to find useless directions
    opposites = {"NORTH": "SOUTH", "SOUTH": "NORTH", "WEST": "EAST", "EAST": "WEST"}
    # New list to put correct directions
    new_directions = []
    # Loop through the whole list of direction
    for i in arr:
        if new_directions and new_directions[-1] == opposites[i]:
            new_directions.pop()
        else:
            new_directions.append(i)
    return new_directions
