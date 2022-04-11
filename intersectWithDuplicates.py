class Solution(object):
    def intersect(self, nums1, nums2):
        m = {}
        for i in nums1:
            if i not in m:
                m[i] = 1
            else:
                m[i]+=1
       
        result = []
        for i in nums2:
            if i in m and m[i]:
                m[i]-=1
                result.append(i)
        return result
    
# Take two lists nums1 and nums2
# calculate the frequency of elements in the list and store them into m
# for each element i in B, if i is present in m, and frequency is non-zero,
# decrease frequency m[i] by 1
# insert i into the resultant array
# return the resultant array
