class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0:
            return '0'

        base7 = []
        negative = num < 0
        n = abs(num)

        while n:
            base7.append(str(n % 7))
            n //= 7

        result =  ''.join(base7[::-1])

        return '-' + result if negative else result
