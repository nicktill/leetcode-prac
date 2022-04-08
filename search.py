class Solution(object):
#LC easy
    def search(self, nums, target):
        left, right = 0, len(nums)-1
        while left <= right:
            pivot = left + (right - left) // 2
            if nums[pivot] == target:
                return pivot
            if target < nums[pivot]:
                right = pivot-1
            if target > nums[pivot]:
                left = pivot+1
        
        return -1