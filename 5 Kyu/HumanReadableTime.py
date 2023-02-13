# Given an integer which represents seconds, return it in
# Hours/Minutes/Seconds format


def make_readable(seconds):
    minute, sec = divmod(seconds, 60)
    hour, minute = divmod(minute, 60)

    # Using .format method to format 00:00:00
    output = '{:02d}:{:02d}:{:02d}'.format(hour, minute, sec)
    return output


print(make_readable(101010))
