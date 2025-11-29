class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        self.total_tilt = 0

        def dfs(node):
            if not node:
                return 0

            left_sum = dfs(node.left)
            right_sum = dfs(node.right)

            node_tilt = abs(left_sum - right_sum)

            self.total_tilt += node_tilt

            return node.val + left_sum + right_sum

        dfs(root)
        return self.total_tilt
