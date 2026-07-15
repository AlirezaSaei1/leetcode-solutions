class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        def gcd(a, b):
            while b != 0:
                a, b = b, a % b
            return a
        
        sum_even = n * (n + 1)
        sum_odd = n ** 2

        return gcd(sum_odd, sum_even)
