#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the getWays function below.
def getWays(n, c):
    temp={}
    p=countWays(0,n,c,temp)
    print(p)
    return p

def countWays(i,n,c,temp):
    key=str(i)+" "+str(n)
    if key in temp:
        return temp[key]
    if n<0:
        return 0
    if n==0:
        return 1
    if n!=0 and i>=len(c):
        return 0

    include=countWays(i,n-c[i], c,temp)
    exclude=countWays(i+1,n,c,temp)
    temp[key]=include+exclude
    return temp[key]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    c = list(map(int, input().rstrip().split()))

    # Print the number of ways of making change for 'n' units using coins having the values given by 'c'

    ways = getWays(n, c)
    fptr.write(str(ways))

    fptr.close()
