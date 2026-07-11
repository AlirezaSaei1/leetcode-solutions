class Solution:
    def processStr(self, s: str, k: int) -> str:
        curr_len = 0
        for char in s:
            if char == '*':
                if curr_len > 0:
                    curr_len -= 1
            elif char == '#':
                curr_len *= 2
            elif char == '%':
                continue
            else:
                curr_len += 1
        
        if k < 0 or k >= curr_len:
            return '.'

        for char in reversed(s):
            if char == '*':
                curr_len += 1
                
            elif char == '#':
                curr_len //= 2
                if k >= curr_len:
                    k -= curr_len
                    
            elif char == '%':
                k = curr_len - 1 - k
                
            else:
                curr_len -= 1
                if k == curr_len:
                    return char
                    
        return '.'