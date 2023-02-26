def twoSum(nums,target)
    #create a dictionary to store the values and their indices
    dict = {}
    #loop through the list
    for i in range(len(nums)):
        #if the target - the current value is in the dictionary, return the indices
        if target - nums[i] in dict:
            return [dict[target - nums[i]], i]
        #otherwise, add the value and its index to the dictionary
        else:
            dict[nums[i]] = i