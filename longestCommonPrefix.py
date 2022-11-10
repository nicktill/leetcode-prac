class Solution(object):
    def longestCommonPrefix(self, strs):
        if strs is None: 
            return ""
        if len(strs) == 1: 
            return strs[0]
        shortest = min(strs, key=len)
        for i in range(len(shortest)):
            for s in strs: 
                if shortest[i] != s[i]:    
                    return shortest[0:i] #return indexes from 0 to i where the indexes no longer equal
                    
        return shortest #return output