class Solution:
    def reverseDegree(self, s: str) -> int:
        answer = 0
        n = len(s)
        z = ord('z')

        for i in range(n):
            answer += (i + 1) * (z - ord(s[i]) + 1)
        
        return answer