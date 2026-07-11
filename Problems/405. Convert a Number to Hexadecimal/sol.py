class Solution:
    def toHex(self, num: int) -> str:
        if num == 0:
            return "0"

        hex_chars = "0123456789abcdef"

        if num < 0:
            num += 2 ** 32

        result = []
        
        while num > 0:
            hex_digit = num & 0xf
            result.append(hex_chars[hex_digit])
            num >>= 4 

        return ''.join(reversed(result))
        