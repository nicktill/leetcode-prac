def twoSum(nums, target):
    #twoSum solution
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
    
    #optimized solution 
def twoSum(nums, target):
    d = {}
    for i in range(len(nums)):
        if target - nums[i] in d:
            return [d[target - nums[i]], i]
        d[nums[i]] = i

