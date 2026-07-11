class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        rows = len(matrix)
        cols = len(matrix[0])
        max_area = 0

        for r in range(1, rows):
            for c in range(cols):
                if matrix[r][c] == 1:
                    matrix[r][c] += matrix[r-1][c]

        for r in range(rows):
            current_row_heights = sorted(matrix[r], reverse=True)
            
            for i in range(cols):
                height = current_row_heights[i]
                width = i + 1
                area = height * width
                max_area = max(max_area, area)
                
        return max_area