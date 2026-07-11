class Solution:
    def processStr(self, s: str) -> str:
        result = []

        for char in s:
            if char == '*':
                if len(result) > 0:
                    result.pop()
            elif char == '#':
                result = result + result
            elif char == '%':
                result = result[::-1]
            else:
                result.append(char)
        
        return ''.join(result)