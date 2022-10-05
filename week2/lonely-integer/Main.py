#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'lonelyinteger' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def lonelyinteger(a):
    # Write your code here  
    new_arr = a.copy()
    print (a)
    print (new_arr)
    i=0
    j=1
    while j<len(new_arr):
        if new_arr[i]==new_arr[j]:
            print ('index:',i,j)
            print ('element:',new_arr[i],new_arr[j])
            new_arr.pop(i)
            new_arr.pop(j-1)
            print(new_arr)
            j=0
        else:
            print ('index:',i,j)
            print ('element:',new_arr[i],new_arr[j])
        j+=1
    return new_arr[0]
# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

#     n = int(input().strip())

#     a = list(map(int, input().rstrip().split()))

#     result = lonelyinteger(a)

#     fptr.write(str(result) + '\n')

#     fptr.close()

print(lonelyinteger([1,2,3,4,3,2,1]))
# print(lonelyinteger([0,0,1,2,1]))