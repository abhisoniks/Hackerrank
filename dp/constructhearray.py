#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countArray function below.
def countArray(n, k, x):
    a=[0]*n
    b=[0]*n
    if x==1:
        a[0]=1
        b[0]=0
    else:
        a[0]=0
        b[0]=1
    p=pow(10,9)+7
    for i in range(1,n):
        a[i]=(b[i-1]) %(p)
        b[i]=(a[i-1]*(k-1) + b[i-1]*(k-2))%p
    return a[n-1] % p

def count(A,n,k,x,temp,index,preindex):
    counter=0
    if A[index]==A[preindex]:
        return 0
    if index+1<len(A) and A[index+1]==A[index]:
        return 0
    for i in range(1,k+1):
        counter+=count(A,n,k,x,temp,i,i)



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nkx = input().split()

    n = int(nkx[0])

    k = int(nkx[1])

    x = int(nkx[2])

    answer = countArray(n, k, x)

    fptr.write(str(answer) + '\n')

    fptr.close()
