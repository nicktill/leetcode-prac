class Solution(object):
    def longestCommonPrefix(self, strs):
        if len(strs) == 0:
            return ""
        if len(strs) == 1:
            return strs[0]

        # find the shortest string
        shortest = min(strs, key=len)
        # iterate through each char in shortest
        for i in range(len(shortest)):
            for s in strs:
                if s[i] != shortest[i]: #if curr char in shortest is not equal to curr char in s
                    return shortest[:i] # return shortest from 0 to i
        return shortest 