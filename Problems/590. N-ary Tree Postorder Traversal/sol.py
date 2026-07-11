"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        self.nodes = []
        def traverse_postorder(node):
            if not node:
                return

            for child in node.children:
                traverse_postorder(child)

            self.nodes.append(node.val)
        
        traverse_postorder(root)
        return self.nodes