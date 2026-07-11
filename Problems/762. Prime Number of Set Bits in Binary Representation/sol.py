from math import sqrt

class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        
        def is_prime(number):
            if number <= 1:
                return False
            for i in range(2, int(sqrt(number)) + 1):
                if number % i == 0:
                    return False
            return True

        prime_set_bits = {i for i in range(21) if is_prime(i)}

        count = 0
        for num in range(left, right + 1):
            set_bits = bin(num).count('1')
            if set_bits in prime_set_bits:
                count += 1
        
        return count
