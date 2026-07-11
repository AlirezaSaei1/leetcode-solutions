class Solution:
    def addDigits(self, num: int) -> int:
        def sum_digits(number):
            summ = 0 
            while number > 0:
                summ += number % 10
                number = number // 10
            return summ

        while not num//10 == 0:
            num = sum_digits(num)

        return num 