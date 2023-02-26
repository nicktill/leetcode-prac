# #A ninia word is a word which hides in a sentence: it will appear continuously, but must be broken up by one or more spaces.
# For example, the word "star" is a ninja word in the phrase "best artist", but is NOT a ninja word in the phrase "twinkle twinkle little star". (Ninja words must be hidden, and thus always contain spaces).
# Ninja words and the sentences they appear in will always be case-insensitive.
# In addition, sentences may contain ninja stars (denoted with an asterisk "*"). Ninja stars can be any character, including a space.
# Given a list of possible ninja words, and a target sentence, return the score of the ninja words that appear in the sentence, according to the rules below.
#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'countNinjaWords' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING_ARRAY targetWords
#  2. STRING sentence
#

def countNinjaWords(targetWords, sentence):
    # Write your code here
    #create a list of all the words in the sentence
    

    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    targetWords_count = int(input().strip())

    targetWords = []

    for _ in range(targetWords_count):
        targetWords_item = input()
        targetWords.append(targetWords_item)

    sentence = input()

    result = countNinjaWords(targetWords, sentence)

    fptr.write(str(result) + '\n')

    fptr.close()
    
