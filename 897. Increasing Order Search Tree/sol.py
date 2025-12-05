# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def inorder(node):
            if not node:
                return
            yield from inorder(node.left)
            yield node
            yield from inorder(node.right)

        
        dummy = TreeNode(-1)
        curr = dummy
        for node in inorder(root):
            node.left = None
            curr.right = node
            curr = node
        return dummy.right