class Solution:
    def maximumProfit(self, prices: List[int], k: int) -> int:
        NEG = -10**30
        n = len(prices)

        dp0 = [NEG] * (k + 1)
        dpL = [NEG] * (k + 1)
        dpS = [NEG] * (k + 1)
        dp0[0] = 0

        for p in prices:
            new0 = dp0[:]
            newL = dpL[:]
            newS = dpS[:]

            for t in range(k + 1):
                if dp0[t] != NEG:
                    newL[t] = max(newL[t], dp0[t] - p)
                    newS[t] = max(newS[t], dp0[t] + p)

                if t < k:
                    if dpL[t] != NEG:
                        new0[t + 1] = max(new0[t + 1], dpL[t] + p)
                    if dpS[t] != NEG:
                        new0[t + 1] = max(new0[t + 1], dpS[t] - p)

            dp0, dpL, dpS = new0, newL, newS

        return max(dp0)
