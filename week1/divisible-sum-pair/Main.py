


#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'divisibleSumPairs' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER k
#  3. INTEGER_ARRAY ar
#

def divisibleSumPairs(n, k, ar):
    # Write your code here
    counter=0
    for i in range(n):
        for j in range(n):
            if i!=j and i<j:
                if (ar[i]+ar[j])%k==0:
                    counter+=1
    return counter

# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

#     first_multiple_input = input().rstrip().split()

#     n = int(first_multiple_input[0])

#     k = int(first_multiple_input[1])

#     ar = list(map(int, input().rstrip().split()))

#     result = divisibleSumPairs(n, k, ar)

#     fptr.write(str(result) + '\n')

#     fptr.close()

divisibleSumPairs(6,3,[1,3,2,6,1,2])