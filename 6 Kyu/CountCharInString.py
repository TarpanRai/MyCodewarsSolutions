# Given a string, count the occurrence of characters

def count(string):
    counts = {}
    for i in string:
        if i in counts:
            counts[i] += 1
        else:
            counts[i] = 1
    return counts





# Simpler


from collections import Counter

def count(string):
    return Counter(string)
