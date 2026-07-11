class Solution:
    def minOperations(self, s: str) -> int:
        mismatches_start0 = 0
        for i, ch in enumerate(s):
            expected = '0' if i % 2 == 0 else '1'
            if ch != expected:
                mismatches_start0 += 1

        mismatches_start1 = len(s) - mismatches_start0
        return min(mismatches_start0, mismatches_start1)