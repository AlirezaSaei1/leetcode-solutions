# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        self.nums = []
        def dfs(node, path):
            if not node:
                return

            path = path + [node.val]
            if not node.left and not node.right:
                self.nums.append(path)
                return

            dfs(node.left, path)
            dfs(node.right, path)
        
        dfs(root, [])
        
        result = 0
        for p in self.nums:
            result += int(''.join(str(x) for x in p), 2)
        
        return result