# Find if you scored better than you class average
# Return in boolean value

def better_than_average(class_points, your_points):
    # Get the class average
    avg = sum(class_points) / len(class_points)
    # Check if your score is lower or higher than average
    if your_points > avg:
        return True
    else:
        return False
