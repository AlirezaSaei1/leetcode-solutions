class Solution:
    def toLowerCase(self, s: str) -> str:
        result = ''
        offset = ord('a') - ord('A') 

        for char in s:
            if 65 <= ord(char) <= 90:
                result += chr(ord(char) + offset)
            else:
                result += char

        return result 