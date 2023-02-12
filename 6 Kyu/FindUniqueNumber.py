# Find the unique number in an array
def find_uniq(arr):
    # Sort the array so that the unique number will be at the
    # last or first of the array based on its value
    arr.sort()
    # Compare array position 0 and 1
    # If pos 0 and 1 are same, output position -1
    # If pos 0 and 1 are different, output position 0
    if arr[0] == arr[1]:
        n = arr[-1]
    else:
        n = arr[0]
    return n