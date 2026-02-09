class Solution:
    def arraySign(self, nums: List[int]) -> int:
        negs = 0
        for num in nums:
            if num == 0:
                return 0

            if num < 0:
                negs += 1

        return 1 if negs % 2 == 0 else -1
