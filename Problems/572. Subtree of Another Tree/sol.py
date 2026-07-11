# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def serialize(node):
            if not node:
                return "#"
            return f",{node.val}" + serialize(node.left) + serialize(node.right)

        s_root = serialize(root)
        s_sub = serialize(subRoot)

        return s_sub in s_root

        