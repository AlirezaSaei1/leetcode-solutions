class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        return True if num % 10 != 0 or num == 0 else False