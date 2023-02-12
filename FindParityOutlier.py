# Given an array that is entirely composed of odd integers
# or even integers except for a singular integer.
# Find the outlier

def find_outlier(integers):
    # Create 2 arrays to store the even and odd integers
    counter_even = []
    counter_odd = []

    # Separate the odd and even integers
    for i in range(len(integers)):
        if integers[i] % 2 == 0:
            counter_even.append(integers[i])
        else:
            counter_odd.append(integers[i])

    # Return the list that has 1 number in it
    if len(counter_odd) == 1:
        return counter_odd[0]
    else:
        return counter_even[0]