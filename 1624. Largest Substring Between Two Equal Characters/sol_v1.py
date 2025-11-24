class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        maxx = -1
        n = len(s)

        for i in range(97, 123):
            start, end = 0, n - 1

            while start < n:
                if s[start] == chr(i):
                    break
                start += 1
            
            while end > 0:
                if s[end] == chr(i):
                    break
                end -= 1

            if not (start == n or end == -1):
                diff = end - start - 1
                if maxx < diff:
                    maxx = diff
            
        return maxx

