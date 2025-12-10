class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        n, m = len(matrix), len(matrix[0])

        row_mins = [min(row) for row in matrix]

        col_maxs = [max(matrix[i][j] for i in range(n)) for j in range(m)]

        res = [num for num in row_mins if num in col_maxs]
        return res