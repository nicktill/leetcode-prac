/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 
 Given the root of a binary search tree and the lowest and highest boundaries as low and high, trim the tree so that all its elements lies in [low, high]. Trimming the tree should not change the relative structure of the elements that will remain in the tree (i.e., any node's descendant should remain a descendant). It can be proven that there is a unique answer.

Return the root of the trimmed binary search tree. Note that the root may change depending on the given bounds.

https://leetcode.com/problems/trim-a-binary-search-tree/
 */

class Solution {
    public TreeNode trimBST(TreeNode root, int low, int high) {
        if (root == null) return root; //if root null return null
        
        //if the current value is higher than high, we need to pass in root.left value 
        //since the current value needs to be removed and we want to try next smallest value
        if (root.val > high) return trimBST(root.left, low, high); 
        //if the current value is lower than low, we need to pass in root.right value 
        //since the current value needs to be removed and we want to try next largest value
        if (root.val < low) return trimBST(root.right, low, high);
        
        //set root.left and root.right accordingly to update tree
        root.left = trimBST(root.left, low, high);
        root.right = trimBST(root.right, low, high);
        
        return root;
    }
}