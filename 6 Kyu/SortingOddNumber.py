# Given an array of integers, sort the odd numbers in ascending order
# but do not touch the even number and their positions.

def sort_array(source_array):
    # Create new array to put all the odd number into and sort them
    odd_arr = []
    for i in range(len(source_array)):
        if source_array[i] % 2 != 0:
            odd_arr.append(source_array[i])
            print(odd_arr)
    odd_arr.sort()
    z = 0
    # Loop through given array and if the integer is odd replace with
    # the sorted odd array
    for x in range(len(source_array)):
        if source_array[x] % 2 != 0:
            source_array[x] = odd_arr[z]
            z += 1
    return source_array

