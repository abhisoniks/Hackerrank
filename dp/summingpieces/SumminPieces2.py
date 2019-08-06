#!/bin/python3

import os
import sys

def summingPieces(arr2):
    l=len(arr2)
    arr=[0]*len(arr2)
    arr[0]=pow(2,l,1000000007)-1
    p=l-2
    q=0
    for i in range(1,int(l/2)+1):
        arr[i]=(arr[i-1]+pow(2,p,1000000007)-pow(2,q,1000000007))
        p-=1
        q+=1

    i=1
    while arr[l-i]==0:
        arr[l-i]=arr[i-1]
        i+=1

    p=[ arr[i]*arr2[i]  for i in range(len(arr))]
    return sum(p)%1000000007


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = summingPieces(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
