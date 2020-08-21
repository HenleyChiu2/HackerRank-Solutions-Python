#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the appendAndDelete function below.
def appendAndDelete(s, t, k):
    start = 0
    ind = 0
    to_app = 0
    to_del = 0

    while ind < len(s) and ind < len(t) and s[ind] == t[ind]:
        start += 1
        ind += 1

    if start < len(s):
        to_del = len(s[start:])
        if to_del == len(s) and k - to_del >= len(t):
            return 'Yes'
    
    if start < len(t):
        to_app = len(t[start:])

    k -= to_del + to_app

    if k == 0 or (k > 0 and k% 2 == 0) or k >= 2*len(t):
        return 'Yes'

    return 'No'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    t = input()

    k = int(input())

    result = appendAndDelete(s, t, k)

    fptr.write(result + '\n')

    fptr.close()