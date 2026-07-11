class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        total_sum = 0
        neg_count = 0
        min_abs = float('inf')

        for row in matrix:
            for value in row:
                av = abs(value)
                total_sum += av
                neg_count += value < 0
                min_abs = min(min_abs, av)

        if neg_count & 1:
            total_sum -= 2 * min_abs

        return total_sum
