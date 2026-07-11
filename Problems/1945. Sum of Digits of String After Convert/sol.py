class Solution:
    def getLucky(self, s: str, k: int) -> int:
        number = ''.join(str(ord(c) - ord('a') + 1) for c in s)
        
        for _ in range(k):
            number = str(sum(int(d) for d in number))
        
        return int(number)