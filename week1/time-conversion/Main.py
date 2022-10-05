# Given a time in -hour AM/PM format, convert it to military (24-hour) time.

# Note: - 12:00:00AM on a 12-hour clock is 00:00:00 on a 24-hour clock.
# - 12:00:00PM on a 12-hour clock is 12:00:00 on a 24-hour clock.

# Example

# s='12:01:00PM'
# Return '12:01:00'.

# s='12:01:00AM'
# Return '00:01:00'.

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    # Write your code here
    time_array=list(s)
    hour=s[0:2]
    am_pm=s[8:]
    time_array[8:]=''
    if hour=='12' and am_pm=='AM':
        time_array[0:2]='00'
        converted_time=''.join(time_array)
        return converted_time
    elif hour=='12' and am_pm=='PM':
        converted_time=''.join(time_array)
        return converted_time
    elif int(hour)<12 and am_pm=='PM':
        hour24_format=str((int(''.join(time_array[0:2]))+12))
        time_array[0:2]=hour24_format
        converted_time=''.join(time_array)
        return converted_time
    else :
        converted_time=''.join(time_array)
        return converted_time


print (timeConversion('12:05:45PM'))
print (timeConversion('06:05:45PM'))
print (timeConversion('12:00:00PM'))
print (timeConversion('12:01:00PM'))
print (timeConversion('12:00:00AM'))
print (timeConversion('12:05:00AM'))
print (timeConversion('04:59:59AM'))
# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

#     s = input()

#     result = timeConversion(s)

#     fptr.write(result + '\n')

#     fptr.close()