class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        def nozero(m):
            while m > 0:
                digit = m % 10
                if digit == 0:
                    return False
                m //= 10
            return True 

        for i in range(1, n):
            if nozero(i) and nozero(n - i):
                return [i, n - i] 