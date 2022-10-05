# Given five positive integers, find the minimum and maximum values that can be calculated by summing exactly four of the five integers. Then print the respective minimum and maximum values as a single line of two space-separated long integers.

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    # Write your code here
    min_value=min(arr)
    max_value=max(arr)
    min_array=arr.copy()
    max_array=arr.copy()
    min_array.pop(min_array.index(max_value))
    max_array.pop(max_array.index(min_value))
    total_min=0
    total_max=0
    for x in min_array:
        total_min+=x
    for x in max_array:
        total_max+=x
    print (total_min,total_max)
if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)