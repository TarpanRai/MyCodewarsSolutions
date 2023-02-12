# Given an array, move all the 0s to the end
# Keep the order of the other numbers

def move_zeros(lst):
    # Loop through array and if the integer is 0,
    # remove it and append a 0 to the back
    for i in lst:
        if i == 0:
            lst.remove(i)
            lst.append(i)
    return lst
