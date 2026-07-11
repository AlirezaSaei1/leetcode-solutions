# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        nodes = []
        def recursive(node):
            if not node:
                return 

            nodes.append(node.val)

            recursive(node.left)
            recursive(node.right)

        recursive(root)
        return nodes

        