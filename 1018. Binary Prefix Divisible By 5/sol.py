class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        results = []
        current = 0
        for bit in nums:
            current = (current * 2 + bit) % 5
            results.append(current == 0)
        return results