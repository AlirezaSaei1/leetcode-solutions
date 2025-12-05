class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        summ = 0
        def traverse(node):
            nonlocal summ
            if not node:
                return

            if node.val > low:
                traverse(node.left)

            if low <= node.val <= high:
                summ += node.val

            if node.val < high:
                traverse(node.right)

        traverse(root)
        return summ
