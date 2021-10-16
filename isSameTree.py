 def isSameTree(self, p, q):
        if not p and not q:
            return True
        if not p or not q:
            return False
        if p.val != q.val: 
            return False
        #otherwise call the function back on left childs, and right childs
        return self.isSameTree(p.right, q.right) and \
        self.isSameTree(p.left, q.left) 
        
        