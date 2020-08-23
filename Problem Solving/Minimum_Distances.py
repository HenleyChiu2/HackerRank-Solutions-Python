#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumDistances function below.
def minimumDistances(a):
    min_distance = len(a)

    for i in range(len(a)):
        for j in range(i+1, len(a)):
            if a[i] == a[j]:
                min_distance = min(min_distance, j-i)

    if min_distance == len(a):
        return -1
    return min_distance

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    a = list(map(int, input().rstrip().split()))

    result = minimumDistances(a)

    fptr.write(str(result) + '\n')

    fptr.close()