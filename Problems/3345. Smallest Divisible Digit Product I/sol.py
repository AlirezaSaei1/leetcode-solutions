class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        def digit_product(number):
            product = 1
            while number > 0:
                digit = number % 10
                if digit == 0: return 0
                product *= digit
                number //= 10
            
            return product

        for i in range(11):
            if digit_product(n + i) % t == 0 :
                return n + i