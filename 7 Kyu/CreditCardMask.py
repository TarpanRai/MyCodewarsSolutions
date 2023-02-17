# Given a string, mask all characters except the last 4

def maskify(cc):
    return cc[-4:].rjust(len(cc), '#')
