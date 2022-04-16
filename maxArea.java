// You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
// Find two lines that together with the x-axis form a container, such that the container contains the most water.
// Return the maximum amount of water a container can store.
// Notice that you may not slant the container.
//LC Med https://leetcode.com/problems/container-with-most-water/
public class Solution {
    public int maxArea(int[] height) {
        int maxarea = 0, l = 0, r = height.length - 1;
        
        while (l < r) {
            int frameMax = Math.min(height[l], height[r]) * (r - l);
            maxarea = Math.max(maxarea, frameMax);
            if (height[l] < height[r])
                l++;
            else
                r--;
        }
        return maxarea;
    }
}
// Unoptimized (time limit exceeded)
// class Solution {
//     public int maxArea(int[] height) {
//         int currMax =0;
//         int distance = 0; 
//         int _height = 0; 
//         int frameMax = 0; 
//         for(int i =0; i < height.length; i++){
//             for(int j = i+1; j < height.length; j++){
//                 //area is equal to distance time minHeight of two indexes  
//                 distance = j-i;
//                 _height = Math.min(height[i], height[j]);
//                 frameMax = distance*_height; 
//                 currMax = Math.max(currMax, frameMax);
                
//             }
//         }
        
//         return currMax;
//     }
// }