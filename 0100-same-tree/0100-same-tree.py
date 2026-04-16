# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def isSameTree(self, p, q):
        # Case 1: dono null hain
        if not p and not q:
            return True
        
        # Case 2: ek null hai, ek nahi
        if not p or not q:
            return False
        
        # Case 3: value check + left + right
        if p.val == q.val:
            return (self.isSameTree(p.left, q.left) and 
                    self.isSameTree(p.right, q.right))
        
        # value same nahi hai
        return False