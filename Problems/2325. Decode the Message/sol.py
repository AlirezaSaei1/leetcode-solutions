class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        mapping = {' ': ' '}
        curr_char = ord('a')
        
        for char in key:
            if char not in mapping:
                mapping[char] = chr(curr_char)
                curr_char += 1
                
        return ''.join(mapping[char] for char in message)