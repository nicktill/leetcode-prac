public void rotate(int[] nums, int k) {
    int[] a = new int[nums.length];
    for (int i = 0; i < nums.length; i++) {
      a[(i + k) % nums.length] = nums[i]; //when the index allocated is higher than nums/length, we will get the overflow value
      //which is equivilent to the shifted position
    }
      
    for(int i = 0; i < nums.length; i++){
        nums[i] = a[i];
    }
      
    System.out.print(nums);
  }
}