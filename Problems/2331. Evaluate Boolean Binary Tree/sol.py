# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def evaluateTree(self, root: TreeNode | None) -> bool:
        def check(node):
            if node.val == 2:
                return check(node.left) or check(node.right)
            elif node.val == 3:
                return check(node.left) and check(node.right)
            else:
                if node.val == 0:
                    return False
                else:
                    return True
        
        return check(root)