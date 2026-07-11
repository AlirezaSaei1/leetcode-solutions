# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        prev = None
        min_diff = float('inf')

        def inorder(node):
            nonlocal prev, min_diff
            if not node:
                return

            inorder(node.left)
            if prev is not None:
                cur_diff = (node.val - prev)
                if min_diff > cur_diff:
                    min_diff = cur_diff
            prev = node.val
            inorder(node.right)

        inorder(root)
        return min_diff