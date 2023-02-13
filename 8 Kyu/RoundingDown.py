# Nathan drinks 0.5 liters of water per hour of cycling
# Given a time in hours, return the number of liters nathan will drink


# Hm... found that when u do int it will round it down
# Much easier than using the math function
def litres(time):
    return int(time * 0.5)
