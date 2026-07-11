class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        total_sum = 0
        neg_count = 0
        min_abs = float('inf')

        for i in range(n):
            for j in range(n):
                value = matrix[i][j]
                av = abs(value)
                total_sum += av

                if value < 0:
                    neg_count += 1

                min_abs = min(min_abs, av)

        if neg_count % 2 == 1:
            total_sum -= 2 * min_abs

        return total_sum
