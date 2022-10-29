# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderSuccessor(self, root, p):
        successor = None 
        while(root): #check if the node p value is greater than root
            #if it is greater than root, we can discard the entire left side of tree
            if(p.val >= root.val): #as inOrderSuccessor wants the smallest value greater than p
                root = root.right #move root to right
            else: #if p.val < node.val, implies that the successor must lie in the left subtree
                successor = root #we update our local variable for keeping track of the successor
                root = root.left #and move all the way left to find the smallest value 
                #if it ends up being null we just return the most recently updated successsor
            
        return successor


    
        