# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution(object):
    def rightSideView(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        
        if not root:
            return []
        
        result = []
        q = deque([root])
        
        while q:
            level_size = len(q)
            
            for i in range(level_size):
                node = q.popleft()
                
                # Last node of current level
                if i == level_size - 1:
                    result.append(node.val)
                
                if node.left:
                    q.append(node.left)
                
                if node.right:
                    q.append(node.right)
        
        return result