# Given an array, count the number of smiling faces.
# Each smiley face must contain a valid pair of eyes.
# Eyes can be marked as : or ;
# A smiley face can have a nose, but it does not have to.
# Valid characters for a nose are - or ~
# Every smiling face must have a smiling mouth that should be marked with either ) or D

import re


def count_smileys(arr):
    # Use regEx
    # [;:][-~][)D]: [; or :] [- or ~]*or neither [) or D]
    valid_Smiles = r"[;:][-~][)D]"
    return len(re.findall(valid_Smiles, arr))
