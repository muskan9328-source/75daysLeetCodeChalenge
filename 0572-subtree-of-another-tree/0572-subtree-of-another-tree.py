class Solution(object):
    
    # Step 1: Check if two trees are identical
    def isSame(self, s, t):
        if not s and not t:
            return True
        if not s or not t:
            return False
        if s.val != t.val:
            return False
        
        return self.isSame(s.left, t.left) and self.isSame(s.right, t.right)
    
    # Step 2: Check subtree
    def isSubtree(self, root, subRoot):
        if not root:
            return False
        
        # check at current node
        if self.isSame(root, subRoot):
            return True
        
        # check left and right
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)