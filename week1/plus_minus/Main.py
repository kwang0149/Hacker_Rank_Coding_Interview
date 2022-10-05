#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here
    positive_digit=0
    negative_digit=0
    zero=0
    n=len(arr)
    for x in arr:
        if x>0:
            positive_digit+=1
        elif x<0:
            negative_digit+=1
        else:
            zero+=1
    print("{:.6f}".format(positive_digit/n))
    print ("{:.6f}".format(negative_digit/n))
    print ("{:.6f}".format(zero/n))
if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
