class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        column = ""
        while columnNumber > 0:
            columnNumber -= 1
            remainder = columnNumber % 26
            column = chr(remainder + 65) + column
            columnNumber //= 26
        return column