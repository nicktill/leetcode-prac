# For the recursive approach, we maintain some minor "global" state so each recursive call can access and modify the current total sum. Essentially, we ensure that the current node exists, recurse on the right subtree, visit the current node by updating its value and the total sum, and finally recurse on the left subtree. If we know that recursing on root.right properly updates the right subtree and that recursing on root.left properly updates the left subtree, then we are guaranteed to update all nodes with larger values before the current node and all nodes with smaller values after.
#A binary tree has no cycles by definition, so convertBST gets called on each node no more than once. Other than the recursive calls, convertBST does a constant amount of work, so a linear number of calls to convertBST will run in linear time.
#https://leetcode.com/problems/convert-bst-to-greater-tree/solution/
#LC Med

class Solution(object):
    def __init__(self):
        self.total = 0

    def convertBST(self, root):
        if root is not None:
            self.convertBST(root.right)
            self.total += root.val #add current val to self total
            root.val = self.total #set value as total 
            self.convertBST(root.left) #move to next node
        return root