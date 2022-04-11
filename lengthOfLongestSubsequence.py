class Solution(object):
#Medium LC https://leetcode.com/problems/longest-substring-without-repeating-characters/solution/
    def lengthOfLongestSubstring(self, s):
        currLongest = []
        currMax = 0
        for letters in s:
            if letters in currLongest: #if we already seen the letter
                #i.e example string: aabcd
                # currLongest = [a]
                # we are on second index of a, and now we set the second index as starting point 
                #since duplicate characters do not count as subsequence
                currLongest = currLongest[currLongest.index(letters)+1:]  
            
            #base case
            currLongest.append(letters) #if unique add to list
            currMax = max(currMax, len(currLongest)) #check max of currMax and len(currLongest)
        
        return currMax