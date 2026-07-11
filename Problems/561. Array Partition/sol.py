class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        OFFSET = 10000
        freq = [0] * (2 * OFFSET + 1)

        for num in nums:
            freq[num + OFFSET] += 1

        total = 0
        take = True

        for value in range(len(freq)):
            while freq[value] > 0:
                if take:
                    total += value - OFFSET
                take = not take
                freq[value] -= 1

        return total