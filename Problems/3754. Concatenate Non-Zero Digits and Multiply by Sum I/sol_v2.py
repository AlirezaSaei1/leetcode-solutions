class Solution:
    def sumAndMultiply(self, n: int) -> int:
        if n == 0: return 0

        mag = 1
        temp = n
        while temp >= 10:
            mag *= 10
            temp //= 10
            
        summ = 0
        number = 0
        temp = n
        
        while mag > 0:
            digit = (temp // mag) % 10
            if digit != 0:
                summ += digit
                number = (number * 10) + digit
            mag //= 10
            
        return number * summ