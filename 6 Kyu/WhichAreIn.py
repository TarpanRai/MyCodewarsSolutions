# Given two arrays of strings, a1 and a2.
# Return a sorted array in lexicographical order of the string of a1 which are a substring of a2

# Example 1:
# a1 = ["arp", "live", "strong"]
# a2 = ["lively", "alive", "harp", "sharp", "armstrong"]
# returns ["arp", "live", "strong"]

#Example 2:
#a1 = ["tarp", "mice", "bull"]
#a2 = ["lively", "alive", "harp", "sharp", "armstrong"]
#returns []



def in_array(array1, array2):
    output = []
    for i in array1:
        for x in array2:
            if i in x:
                output.append(i)
                break
    return sorted((set(output)))


# 0.o A ONE LINER
def in_array(a1, a2):
    return sorted({sub for sub in a1 if any(sub in s for s in a2)})

