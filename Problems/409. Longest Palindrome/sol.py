class Solution:
    def longestPalindrome(self, s: str) -> int:
        counter = Counter(s)
        is_odd = False
        length = 0
        for i in counter.values():
            if i % 2 != 0:
                is_odd = True
            length += (i // 2) * 2
        
        if is_odd:
            length += 1
        
        return length