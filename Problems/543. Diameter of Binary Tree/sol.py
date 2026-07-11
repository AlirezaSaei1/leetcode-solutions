# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter = 0

        def postorder(node):
            if not node:
                return 0

            depth_left = postorder(node.left)
            depth_right = postorder(node.right)
            
            self.diameter = max(self.diameter, depth_left + depth_right)

            return 1 + max(depth_left, depth_right)

        postorder(root)
        return self.diameter
            