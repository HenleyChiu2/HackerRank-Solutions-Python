#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the acmTeam function below.
def acmTeam(topic):
    maxsub = 0
    count_teams = 0

    for i in range(n):
        for j in range(i, n):
            sub = 0
            for x, y in zip(topic[i], topic[j]):
                if x == '1' or y == '1':
                    sub += 1
            
            if sub > maxsub:
                maxsub = sub
                count_teams = 1
            
            elif sub == maxsub:
                count_teams += 1

    return [maxsub, count_teams]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    topic = []

    for _ in range(n):
        topic_item = input()
        topic.append(topic_item)

    result = acmTeam(topic)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()