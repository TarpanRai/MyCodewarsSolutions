# Remove all non-negative integers and string from array

def filter_list(l):
    return [i for i in l if not isinstance(i, str)]
