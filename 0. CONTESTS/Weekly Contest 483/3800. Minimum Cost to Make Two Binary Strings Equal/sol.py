class Solution:
    def minimumCost(self, s: str, t: str, flipCost: int, swapCost: int, crossCost: int) -> int:
        first_zero, second_zero = 0, 0
        for i in range(len(s)):
            if s[i] == '0' and t[i] == '1':
                first_zero += 1
            elif s[i] == '1' and t[i] == '0':
                second_zero += 1

        total_cost = 0

        mixed_pairs = min(first_zero, second_zero)
        total_cost += mixed_pairs * min(swapCost, 2 * flipCost)

        remaining = abs(first_zero - second_zero)
        same = remaining // 2

        total_cost += same * min(2 * flipCost, crossCost + swapCost)

        if remaining % 2 == 1:
            total_cost += flipCost

        return total_cost
    