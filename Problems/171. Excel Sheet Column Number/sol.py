class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        col_num = 0
        i = 0
        for c in columnTitle[::-1]:
            num = ord(c) - 64
            col_num += (num * (26**i))
            i += 1
        
        return col_num