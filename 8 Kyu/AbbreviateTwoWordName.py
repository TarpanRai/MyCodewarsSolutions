# Given a name, convert it into initials
def abbrev_name(name):
    return '.'.join([i[0].upper() for i in name.split(' ')])
