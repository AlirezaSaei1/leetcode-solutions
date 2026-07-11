class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        min_val = root.val
        self.ans = float('inf')

        def dfs(node):
            if not node:
                return
            if min_val < node.val < self.ans:
                self.ans = node.val
            elif node.val == min_val:
                dfs(node.left)
                dfs(node.right)

        dfs(root)
        return self.ans if self.ans < float('inf') else -1
