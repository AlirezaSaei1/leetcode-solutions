class Solution:
    def reformat(self, s: str) -> str:
        digits = [ch for ch in s if ch.isdigit()]
        letters = [ch for ch in s if ch.isalpha()]
        
        if abs(len(digits) - len(letters)) > 1:
            return ''
        
        if len(letters) > len(digits):
            letters, digits = digits, letters
        
        result = []
        for i in range(max(len(digits), len(letters))):
            result.append(digits[i])
            if i < len(letters):
                result.append(letters[i])
        
        return ''.join(result)