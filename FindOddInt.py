# Given an array, find the one that appears an odd number of times


def find_it(seq):
    dupe_rmv = list(set(seq))
    for i in range(0, len(dupe_rmv)):
        counted = seq.count(dupe_rmv[i])
        if counted % 2 == 0:
            continue
        else:
            return dupe_rmv[i]