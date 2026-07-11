"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        self.nodes = []
        def traverse_preorder(node):
            if not node:
                return
            
            self.nodes.append(node.val)
            for child in node.children:
                traverse_preorder(child)
        
        traverse_preorder(root)
        return self.nodes