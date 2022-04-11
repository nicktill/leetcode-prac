class Solution(object):
    def containsDuplicate(self, nums):
        setLength = len(set(nums))
        if setLength != len(nums): return True
        return False

#Solution using Dictionary:
# class Solution(object):
#     def containsDuplicate(self, nums):
#         dictionary = {}
#         for x in nums:
#             if x in dictionary:
#                 return True
#             else:
#                 dictionary[x]= nums
