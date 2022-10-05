#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'findMedian' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def findMedian(arr):
    # Write your code here
    sorted_arr=arr.copy()
    sorted_arr.sort()
    print (sorted_arr)
    return sorted_arr[int(len(sorted_arr)/2)]

findMedian([0,1,2,4,6,5,3])

    
