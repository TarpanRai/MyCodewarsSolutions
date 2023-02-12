# Given an integer, square individual digits and concatenate them

def square_digits(num):
    squared_num = ''
    for i in str(num):
        squared_num += str(int(i) ** 2)
    return int(squared_num)