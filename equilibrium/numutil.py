import re

def parsefloat(str):
    return float(re.sub('[^0-9.\-]', '', str))