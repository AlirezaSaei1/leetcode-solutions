class Solution:
    def minimumCost(self, cost1: int, cost2: int, costBoth: int, need1: int, need2: int) -> int:
        total = 0

        if costBoth < cost1 + cost2:
            fill = min(need1, need2)
            total += fill * costBoth
            need1 -= fill
            need2 -= fill

        if need1 > 0:
            if costBoth < cost1:
                total += need1 * costBoth
            else:
                total += need1 * cost1

        if need2 > 0:
            if costBoth < cost2:
                total += need2 * costBoth
            else:
                total += need2 * cost2

        return total

        