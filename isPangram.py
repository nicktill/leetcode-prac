#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'isPangram' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING_ARRAY pangram as parameter.
#

def isPangram(pangram):
      # Write your code here
      result = [] #this is our list holding the respective indexes of whether or not string is pangram
      ouputString = '' #need to have an output string to convert to when returning result (does not accept type List)
      for string in pangram: #iterate among the strings in the list
          if len(string) < 26: #if the current length of the string is less than 26, cannot be pangram, append 0
              result.append('0') 
          else: #otherwise, the length minimum is set (i,e len>=26,)
              temp = set() #create a set for no duplicates
              for char in string: #iterate among the letters in the string
                  if char.isalpha(): #if its an alphanumeric character
                      temp.add(char.lower()) #add to our set
              if len(temp) == 26: #if the length of the set is 26, that means we have all letters, therefore append 1
                  result.append('1') 
              else: #else, we do not have all letters so append 0
                  result.append('0')
                  
            #to whoever is reviewing this code, i hope you appreciate the comments! :D
                  
      return ouputString.join(result) #expected output is string, need to convert list to string 
      #otherwise type error occurs on line 50 => concatenating result as a type list, when expecting String

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    pangram_count = int(input().strip())

    pangram = []

    for _ in range(pangram_count):
        pangram_item = input()
        pangram.append(pangram_item)

    result = isPangram(pangram)

    fptr.write(result + '\n')

    fptr.close()
