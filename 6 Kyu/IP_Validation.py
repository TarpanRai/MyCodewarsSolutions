# Write a function that identifies a valid IPv4 address

def is_valid_IP(string):
    ip_split = string.split('.')
    if len(ip_split) != 4:
        return False
    for i in ip_split:
        if not i.isdigit():
            return False
        if len(i) > 1 and i[0] == '0':
            return False
        if int(i) < 0 or int(i) > 255:
            return False
    return True
