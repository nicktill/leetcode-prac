class Solution(object):
#LC Medium
    def maxProduct(self, nums):
        #base check
        if len(nums) == 0:
            return 0
        
        currMax = nums[0] #grab first value of array
        currMin = nums[0]
        result = currMax 
        
        for i in range(1, len(nums)):
            curr = nums[i] #grab second index
            currMax = max(curr, currMax*curr, currMin*curr)
            currMin = min(curr, currMax *curr, currMin*curr)
            result = max(currMax, result)
            
        return result


