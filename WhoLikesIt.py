# Facebook like system

def likes(names):
    if len(names) == 0:
        result = 'no one likes this'
    elif len(names) == 1:
        result = '{} likes this'.format(names[0])
    elif len(names) == 2:
        result = '{} and {} like this'.format(names[0], names[1])
    elif len(names) == 3:
        result = '{}, {} and {} like this'.format(names[0], names[1], names[2])
    else:
        result = '{}, {} and {} others like this'.format(names[0], names[1], len(names) - 2)
    return result
