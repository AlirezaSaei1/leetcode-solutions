class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        n = len(arr)
        mn, mx = min(arr), max(arr)
        if (mx - mn) % (n - 1) != 0:
            return False
        d = (mx - mn) // (n - 1)
        if d == 0:
            return len(set(arr)) == 1
        expected = {mn + i * d for i in range(n)}
        return set(arr) == expected