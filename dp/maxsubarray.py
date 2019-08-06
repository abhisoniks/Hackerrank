#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the maxSubarray function below.
def maxSubarray(arr):
    subsequence=0
    flag=False
    for j in arr:
        if j>0:
            flag=True
            subsequence+=j
    if not flag:
        return [max(arr),max(arr)]

    temp=[0]*len(arr)
    temp[0]=arr[0]
    for i in range(1,len(arr)):
        if arr[i]>arr[i]+temp[i-1]:
            temp[i]=arr[i]
        else:
            temp[i]=arr[i]+temp[i-1]
    subarr=max(temp)
    return [subarr,subsequence]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        arr = list(map(int, input().rstrip().split()))

        result = maxSubarray(arr)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()
