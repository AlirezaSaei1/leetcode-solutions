class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        def is_prime(x):
            if x < 2:
                return False
            for i in range(2, int(x ** 0.5) + 1):
                if x % i == 0:
                    return False
            return True

        ans = 0
        for n in nums:
            # case 1: n = p^3
            p = round(n ** (1/3))
            if p**3 == n and is_prime(p):
                ans += 1 + p + p*p + n
                continue

            # case 2: n = p * q
            for i in range(2, int(n ** 0.5) + 1):
                if n % i == 0:
                    j = n // i
                    if i != j and is_prime(i) and is_prime(j):
                        ans += 1 + i + j + n
                    break
        return ans
