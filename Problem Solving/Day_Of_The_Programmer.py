#!/bin/python3

import math
import os
import random
import re
import sys

def is_leap_year(year):
    if year < 1918:
        if year % 4 == 0:
            return True
    if year % 400 == 0:
        return True
    elif year % 4 == 0 and year % 100 != 0:
        return True
    else:
        return False

# Complete the dayOfProgrammer function below.
def dayOfProgrammer(year):
    if (year >= 1700 and year <= 2700):
        if (year == 1918):
            return '26.09.1918'
        elif is_leap_year(year):
            return '12.09.%s' % year
        else:
            return '13.09.%s' % year
    return ("Incorrect year.")
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    year = int(input().strip())

    result = dayOfProgrammer(year)

    fptr.write(result + '\n')

    fptr.close()
