# Take an array with 10 integers and format it into a phone number

def create_phone_number(n):
    joint = ''
    for i in n:
        joint += str(int(i))
        print(joint)
    cc = '(' + joint[0:3] + ') ' + joint[3:6] + '-' + joint[6:10]
    return cc
