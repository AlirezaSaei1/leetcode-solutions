class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        visited_nodes = []
        for n1, n2 in edges:
            if n1 in visited_nodes:
                return n1
            else:
                visited_nodes.append(n1)
            
            if n2 in visited_nodes:
                return n2
            else:
                visited_nodes.append(n2)
