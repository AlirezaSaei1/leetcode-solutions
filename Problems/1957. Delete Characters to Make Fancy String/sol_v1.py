class Solution:
    def makeFancyString(self, s: str) -> str:
        prev = s[0]
        n = len(s)
        answer = []

        cur = 0
        for i in range(n):
            if s[i] == prev:
                cur += 1
            else:
                cur = 1

            if cur <= 2:
                answer.append(s[i])

            prev = s[i]
        
        return ''.join(answer)