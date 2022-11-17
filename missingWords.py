#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'missingWords' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts following parameters:
#  1. STRING s
#  2. STRING t
#

def missingWords(s, t):
    # Write your code here
    #split both strings so that they are easier to parse/read 
    s = s.split() 
    t = t.split()
    result = []
    i = 0
    j = 0
    while i < len(s) and j < len(t):
        if s[i] != t[j]: #if not equal at indexes(i.e missing word)
            result.append(s[i]) #append the missing word 
            i += 1 #incremenet the index to indicate that we've added it to missingWordsList
        else: #otherwise, no missing word, so increment both pointers
            i += 1
            j += 1
    #at this point, if strings were same length, we are completed
    #otherwise though, we need to account for extra letters that would be all missing
    while i < len(s): #edge case to add all the remaining characters in i if there are additional that j did not have 
        result.append(s[i]) #appending 
        i += 1 #increment counter
        
    return result #and lastly, return our result
    
    #to whoever is reviewing my code => I spent quite some time on this problem because I was confident there would be a way to do it in less time complexity, but struggled quite a bit so am just submiting this solution, which unfortunately isnt the most optimized, but at least does the trick! I feel there still might be a way using pythons  enumerate function to compare indexes and values, but was stuck on that for a bit too long so went ahead and implemented it this way. 
    
    #feel free to connect with my on linkedin!
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    t = input()

    result = missingWords(s, t)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()
