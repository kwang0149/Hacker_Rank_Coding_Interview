#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    # Write your code here
    primary_diagonal=0
    secondary_diagonal=0
    i=0
    j=0
    k=len(arr[0])-1
    while i<len(arr) and j<len(arr[0]) and k>=0:
        primary_diagonal+=arr[i][j]
        secondary_diagonal+=arr[i][k]
        i+=1
        j+=1
        k-=1
    return abs(primary_diagonal-secondary_diagonal)


if __name__ == '__main__':
    fptr = sys.stdout

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
