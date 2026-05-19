# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        
        # Base case
        if root is None:
            return None
        
        # If current node is p or q
        if root == p or root == q:
            return root
        
        # Search in left and right subtree
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        
        # If both sides return something,
        # current node is LCA
        if left and right:
            return root
        
        # Otherwise return non-null side
        return left if left else right