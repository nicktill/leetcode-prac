class Solution {
 public int[] twoSum(int[] nums, int target) {
    Map<Integer, Integer> map = new HashMap<>();
    for (int i = 0; i < nums.length; i++) {
        map.put(nums[i], i); //add key pair values to HashMap, where Key is nums[i], and index is pair value
    }
    for (int i = 0; i < nums.length; i++) {
        int complement = target - nums[i]; //find the complement at each iteration
        if (map.containsKey(complement) && map.get(complement) != i) { //check if value in HashMap, and also that its not nums[i] itself (this would be the same num adding to itself)
            return new int[] { i, map.get(complement) }; //if this is both true return
        }
    }
    throw new IllegalArgumentException("No two sum solution"); //No Two Sum
    }
}
