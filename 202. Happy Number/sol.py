class Solution:
    def isHappy(self, n: int) -> bool:
        def get_next(number):
            total = 0
            while number > 0:
                digit = number % 10
                total += digit * digit
                number //= 10
            return total

        visited = set()
        while n != 1 and n not in visited:
            visited.add(n)
            n = get_next(n)

        return n == 1
