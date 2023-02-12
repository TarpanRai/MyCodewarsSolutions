# Given an integer, return the sum of all the multiples of
# 3 and 5. If number is negative, return 0


def solution(number):
    sum_num = 0
    number -= 1
    while number >= 3:
        if number % 5 == 0 or number % 3 == 0:
            sum_num = sum_num + number
            number -= 1
        else:
            number -= 1
    return sum_num
