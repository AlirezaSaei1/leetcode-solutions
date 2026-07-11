class Solution:
    def rotatedDigits(self, n: int) -> int:
        count = 0
        for i in range(1, n + 1):
            s = str(i)
            # Must not contain 3, 4, or 7
            if any(c in '347' for c in s):
                continue
            # Must contain at least one of 2, 5, 6, or 9
            if any(c in '2569' for c in s):
                count += 1
        return count