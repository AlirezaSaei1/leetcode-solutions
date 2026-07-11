class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        n = len(arr)
        result = 0

        for i in range(n - 2):
            for j in range(i + 1, n - 1):
                if abs(arr[i] - arr[j]) <= a:
                    low = max(arr[j] - b, arr[i] - c)
                    high = min(arr[j] + b, arr[i] + c)
                    for k in range(j + 1, n):
                        if low <= arr[k] <= high:
                            result += 1
        return result
