# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional

class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        def recursive(node):
            if not node:
                return 0
            
            total = 0
            if node.left:
                # Check if it's a leaf
                if not node.left.left and not node.left.right:
                    total += node.left.val
                else:
                    total += recursive(node.left)
            if node.right:
                total += recursive(node.right)
            
            return total

        return recursive(root)
