#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'flippingBits' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts LONG_INTEGER n as parameter.
#
def flippingBits(n):
    # Write your code here
    list_flipped=list(format(n,'032b'))
    for i in range(len(list_flipped)):
        if list_flipped[i]=='1':
            list_flipped[i]='0'
        else:
            list_flipped[i]='1'   
    return int(''.join(list_flipped),2)
print (flippingBits(9))

# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

#     q = int(input().strip())

#     for q_itr in range(q):
#         n = int(input().strip())

#         result = flippingBits(n)

#         fptr.write(str(result) + '\n')

#     fptr.close()
