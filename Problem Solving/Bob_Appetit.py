#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the bonAppetit function below.
def bonAppetit(bill, k, b):
    added_cost = 0
    for i in range(len(bill)):
        if i != k:
            added_cost += bill[i]
    split_cost = added_cost / 2

    if b == split_cost:
        print ('Bon Appetit')
    else:
        print(abs(int(split_cost - b)))

if __name__ == '__main__':
    nk = input().rstrip().split()

    n = int(nk[0])

    k = int(nk[1])

    bill = list(map(int, input().rstrip().split()))

    b = int(input().strip())

    bonAppetit(bill, k, b)
