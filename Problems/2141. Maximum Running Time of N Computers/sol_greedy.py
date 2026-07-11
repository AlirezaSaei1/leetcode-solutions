class Solution:
    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        total = sum(batteries)
        batteries.sort()

        while batteries and batteries[-1] > total // n:
            biggest = batteries.pop()
            total -= biggest
            n -= 1

        return total // n
