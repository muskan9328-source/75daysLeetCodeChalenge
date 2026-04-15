class Solution:
    def maxDepth(self, root):
        # Base case
        if root is None:
            return 0
        
        # Left subtree depth
        left = self.maxDepth(root.left)
        
        # Right subtree depth
        right = self.maxDepth(root.right)
        
        # Return max + 1
        return 1 + max(left, right)