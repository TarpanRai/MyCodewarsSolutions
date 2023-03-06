# Given a month as an integer from 1 to 12.
# Return to which quarter of the year it belongs as an integer number.

def quarter_of(month):
    return (month - 1) // 3 + 1
