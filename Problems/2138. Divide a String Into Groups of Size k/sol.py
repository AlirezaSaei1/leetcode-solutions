class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        n = len(s)
        answer = []

        for i in range(0, n, k):
            answer.append(s[i:i+k])
        
        answer[-1] = answer[-1].ljust(k, fill)
        return answer