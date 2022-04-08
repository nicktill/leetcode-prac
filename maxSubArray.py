class Solution(object):
#LC Easy
    def maxSubArray(self, nums):
        currSubArray = nums[0]
        maxSubArray = nums[0]     
        for num in nums[1:]: #starting at index two since we have index 1 @currSubArray  
            currSubArray = max(num, currSubArray+num)
            maxSubArray = max(currSubArray, maxSubArray)
        
        return maxSubArray