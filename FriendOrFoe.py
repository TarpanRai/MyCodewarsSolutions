# Remove all string in an array with more than 4 characters


def friend(x):
    # Create a new array that will contain string with length 4
    new_arr = []
    for i in range(len(x)):
        if len(x[i]) == 4:
            new_arr.append(x[i])
    return new_arr
