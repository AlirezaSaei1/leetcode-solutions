class Solution:
    def sumAndMultiply(self, n: int) -> int:
        number = 0
        summ = 0
        for char in str(n):
            if char == '0':
                continue
            else:
                int_digit = int(char)
                summ += int_digit
                number = (number * 10) + int_digit
        
        return number * summ