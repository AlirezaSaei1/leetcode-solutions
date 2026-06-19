class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        n = len(matrix)
        
        for i in range(n):
            if len(set(matrix[i])) != n:
                return False

            col = [matrix[r][i] for r in range(n)]
            if len(set(col)) != n:
                return False
                
        return True
