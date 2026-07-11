class Solution:
    def largestPrime(self, n: int) -> int:
        def is_prime(n):
            if n <= 1:
                return False

            for i in range(2, int(sqrt(n))+1):
                if n % i == 0:
                    return False

            return True

        primes = []
        mask = [1] * (n + 1)
        for i in range(2, n+1):
            if mask[i] == 1:
                primes.append(i)
                j = i * i
                while j < n+1:
                    mask[j] = 0
                    j += i

        summ = 0
        answer = 0
        for p in primes:
            if summ + p <= n:
                summ += p
                if summ > n:
                    break

                if is_prime(summ):
                    answer = summ

        return answer