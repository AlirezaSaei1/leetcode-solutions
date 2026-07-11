# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        q = deque([(root, None)])

        while q:
            level_size = len(q)
            parent_x = parent_y = None
            
            for _ in range(level_size):
                node, parent = q.popleft()
                if node.val == x:
                    parent_x = parent
                if node.val == y:
                    parent_y = parent

                if node.left:
                    q.append((node.left, node))
                if node.right:
                    q.append((node.right, node))
            
            if parent_x and parent_y:
                return parent_x != parent_y
            if parent_x or parent_y:
                return False

        return False
