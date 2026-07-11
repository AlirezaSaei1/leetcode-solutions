# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        paths = []

        def recursive(node, strr):
            if not node:
                return
            if not node.left and not node.right:
                strr += f'{node.val}'
                paths.append(strr)
            else:
                strr += f'{node.val}->'

                recursive(node.right, strr)
                recursive(node.left, strr)
        
        recursive(root, "")
        return paths