#!/bin/python3


#Solution is with dp . Won't work
import math
import os
import random
import re
import sys

#
# Complete the 'stockmax' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts INTEGER_ARRAY prices as parameter.
#

def stockmax(prices):
    temp={}
    return getProfit(prices,0,0,temp)

def getProfit(prices,i,stock,temp):
    key=str(i)+str(stock)
    if key in temp:
        return temp[key]
    if i>=len(prices):
        return 0
    if i==len(prices)-1:
        return stock*prices[i]
    sell=-1*sys.maxsize
    buy=-prices[i]+getProfit(prices,i+1,stock+1,temp)
    if stock>0:
        sell=(stock*prices[i])+getProfit(prices,i+1,0,temp)
    nothing=getProfit(prices,i+1,0,temp)
    temp[key] =max(buy,sell,nothing)
    return temp[key]



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        prices = list(map(int, input().rstrip().split()))

        result = stockmax(prices)

        fptr.write(str(result) + '\n')

    fptr.close()
