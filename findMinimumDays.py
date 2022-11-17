#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'findMinimumDays' function below.
#
# The function is expected to return an INTEGER.
# The function accepts FLOAT_ARRAY durations as parameter.
#

def findMinimumDays(durations):
    # Write your code here
    durations.sort() #sort the array so that we can compare smallest and largest movie times
    days = 0 #numb days
    endIndex = len(durations) - 1 #end index [1, 2, 3, 4 ,5] i.e 5 in this case
    startIndex = 0 #start index [1, 2, 3, 4 ,5] i.e 1 in this case
    while startIndex <= endIndex: #while start is less than end compares smallest to largest indexes and moves inwards
        if durations[startIndex] + durations[endIndex] <= 3.00: #if smallest + largest movie is less than 3
            startIndex += 1 #iterate start index up
            endIndex -= 1 #iterate end index down
            days += 1 #increase days
        else: #else, we know that we can only watch it in one day,
            endIndex -= 1 #so move ending pointer down
            days += 1 #and account for numb days

    return days #lastly, return our days which is updated!
        
        
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    durations_count = int(input().strip())

    durations = []

    for _ in range(durations_count):
        durations_item = float(input().strip())
        durations.append(durations_item)

    result = findMinimumDays(durations)

    fptr.write(str(result) + '\n')

    fptr.close()
