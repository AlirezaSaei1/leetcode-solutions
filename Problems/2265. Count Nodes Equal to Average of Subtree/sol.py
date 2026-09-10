class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        matching_nodes = 0

        def post_order(node):
            nonlocal matching_nodes
            if not node:
                return (0, 0)

            left_sum, left_count = post_order(node.left)
            right_sum, right_count = post_order(node.right)

            total_sum = left_sum + right_sum + node.val
            total_count = left_count + right_count + 1

            if total_sum // total_count == node.val:
                matching_nodes += 1

            return (total_sum, total_count)

        post_order(root)
        return matching_nodes