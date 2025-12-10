class Solution:
    def thousandSeparator(self, n: int) -> str:
        s = str(n)
        res = []

        for i in range(len(s)):
            res.append(s[~i])
        
            if i % 3 == 2 and i != len(s) - 1:
                res.append('.')

        return ''.join(res[::-1])