class Solution(object):
    def hasPathSum(self, root, targetSum):
        
        # Base case: empty tree
        if not root:
            return False
        
        # If leaf node, check sum
        if not root.left and not root.right:
            return targetSum == root.val
        
        # Recursively check left & right
        return (self.hasPathSum(root.left, targetSum - root.val) or
                self.hasPathSum(root.right, targetSum - root.val))