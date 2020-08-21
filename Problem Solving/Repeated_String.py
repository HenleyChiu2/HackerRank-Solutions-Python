#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the repeatedString function below.
def repeatedString(s, n):
    count = 0
    remainder = n % len(s)

    for a in s:
        if a == 'a':
            count += 1
    
    count *= n // len(s)

    for i in range(remainder):
        if s[i] == 'a':
            count += 1

    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()