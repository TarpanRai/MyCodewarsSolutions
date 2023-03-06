
def greet(name, owner):
    if name == owner:
        return "Hello boss"
    else:
        return "Hello guest"


# Shorter way
def greet(name, owner):
    return "Hello boss" if name == owner else "Hello guest"
