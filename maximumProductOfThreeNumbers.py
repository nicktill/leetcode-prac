class Solution(object):
    def maximumProduct(self, nums):
        nums.sort()
        #first arg is largest 3 values, second arg is top 2 most negative values * largest value
        return max(nums[len(nums)-1] * nums[len(nums)-2] * nums[len(nums)-3], nums[0] * nums[1] * nums[len(nums)-1])