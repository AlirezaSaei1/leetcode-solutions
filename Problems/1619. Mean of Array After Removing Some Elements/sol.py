class Solution:
    def trimMean(self, arr: List[int]) -> float:
        n = len(arr)
        arr.sort()
        idx = n // 20 
        return sum(arr[idx:-idx]) / (n - 2*idx)