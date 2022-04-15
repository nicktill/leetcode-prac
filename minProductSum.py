#https://leetcode.com/problems/minimize-product-sum-of-two-arrays/
#Med

class Solution(object):
    def minProductSum(self, nums1, nums2):
        #calculating minimum product of arrays 
        #sort one ascending and other descending, 
        #so we multiply largest numbers with smallest to get smallest sum
        nums1.sort() 
        nums2.sort(reverse=True)
        sum = 0
        for num1, num2 in zip(nums1, nums2): #use zip to iterate among two idxs in two lists
            sum += num1 * num2

        return sum