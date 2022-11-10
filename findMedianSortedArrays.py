class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        nums = nums1 + nums2 #add all nums to nums array
        nums.sort() #sort the array
        if len(nums) % 2 == 0: #if the array len is even
            return (nums[len(nums) / 2 - 1] + nums[len(nums) / 2]) / 2.0 #if even find two middle elements, add together and divide by 2
        else:
            return nums[len(nums) / 2] #otherise just return the length divided by 2