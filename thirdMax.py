#https://leetcode.com/problems/third-maximum-number/submissions/
#LC Easy
#Given an integer array nums, return the third distinct maximum number in this array. If the third maximum does not exist, return the maximum number.
# Input: nums = [3,2,1]
# Input: nums = [2,2,3,1]
# Output: 1 (because the 2s are not distinct)
class Solution(object):
    def thirdMax(self, nums):
        # Make a set so no duplicates
        nums = set(nums)
        # Find the maximum. 
        maximum = max(nums)
        # Check whether or not this is a case where
        # we need to return the *maximum*.
        if len(nums) < 3:
            return maximum
        # Otherwise, continue on to finding the third maximum.
        nums.remove(maximum) #first removed
        second_maximum = max(nums)
        nums.remove(second_maximum) #second moved
        return max(nums) #this will be third distinct