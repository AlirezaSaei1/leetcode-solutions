class Solution:
    def findMaxVal(self, n: int, restrictions: List[List[int]], diff: List[int]) -> int:
        a = [float('inf')] * n
        a[0] = 0

        for idx, maxVal in restrictions:
            a[idx] = min(a[idx], maxVal)

        for i in range(1, n):
            a[i] = min(a[i], a[i-1] + diff[i-1])

        for i in range(n - 2, -1, -1):
            a[i] = min(a[i], a[i+1] + diff[i])

        return max(a)
        