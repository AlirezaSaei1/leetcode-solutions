# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        nodes = []
        def recursive(node):
            if not node:
                return

            recursive(node.left)
            recursive(node.right)
            nodes.append(node.val)

        recursive(root)
        return nodes