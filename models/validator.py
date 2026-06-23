import re

def validate_string(regex, test_string):

    if re.fullmatch(regex, test_string):
        return "VALID"

    return "INVALID"