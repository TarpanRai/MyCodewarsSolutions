# Given a non-negative integer, 3 for example,
# return a string with a murmur: "1 sheep...2 sheep...3 sheep...".



def count_sheep(num):
    # Use list comprehension
    return ''.join([f"{i} sheep..." for i in range(1, num+1)])
