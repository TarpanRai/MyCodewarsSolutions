# Return true if length of PIN is 4 or 6 else return false

def validate_pin(pin):
    if len(pin) == 4 and pin.isdigit() or len(pin) == 6 and pin.isdigit():
        return True
    else:
        return False
