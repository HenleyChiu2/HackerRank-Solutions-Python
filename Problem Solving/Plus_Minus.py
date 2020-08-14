#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    pos_count = 0
    neg_count = 0
    zero_count = 0

    for num in arr:
        if num > 0:
            pos_count += 1
        elif num == 0:
            zero_count += 1
        else:
            neg_count += 1
    
    print("%.6f" % (pos_count / len(arr)))
    print("%.6f" % (neg_count / len(arr)))
    print("%.6f" % (zero_count / len(arr)))

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)