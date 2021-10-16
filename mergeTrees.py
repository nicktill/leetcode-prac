  def mergeTrees(self, root1, root2):
        if root1 is None:
            return root2
        if root2 is None:
            return root1
        
        #add node of root 2 to same position of root1
        root1.val += root2.val 
        #call the left childs of root1, adding root2.left to it
        root1.left = self.mergeTrees(root1.left, root2.left)
        #call the right childs of root1, adding root2.right to it
        root1.right = self.mergeTrees(root1.right, root2.right)
        
        return root1