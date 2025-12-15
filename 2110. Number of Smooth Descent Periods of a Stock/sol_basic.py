class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        n = len(prices)
        result = 1
        i = 1

        while i < n:
            while i + 1 < n and prices[i] - 1 == prices[i + 1]:
                k += 1
                i += 1

            result += ((k * (k+1)) // 2)
            k = 0
            i += 1
        
        return result + n
