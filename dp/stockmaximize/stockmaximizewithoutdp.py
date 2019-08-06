#!/bin/python3

import math
import os
import random
import re
import sys


def stockmax(prices):
    max_=0
    profit=0
    l=len(prices)-1
    for i in range(l,-1,-1):
        if max_<prices[i]:
            max_=prices[i]
        profit+=max_-prices[i]
    return profit



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        prices = list(map(int, input().rstrip().split()))

        result = stockmax(prices)

        fptr.write(str(result) + '\n')

    fptr.close()
