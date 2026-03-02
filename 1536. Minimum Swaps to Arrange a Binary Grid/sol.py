class Solution:
    def minSwaps(self, grid: List[List[int]]) -> int:
        n = len(grid)

        # Step 1: compute rightmost 1 for each row
        rightmost = []
        for row in grid:
            last = -1
            for i in range(n - 1, -1, -1):
                if row[i] == 1:
                    last = i
                    break
            rightmost.append(last)

        swaps = 0

        # Step 2: greedy placement
        for i in range(n):
            j = i
            while j < n and rightmost[j] > i:
                j += 1

            if j == n:
                return -1

            while j > i:
                rightmost[j], rightmost[j - 1] = rightmost[j - 1], rightmost[j]
                swaps += 1
                j -= 1

        return swaps