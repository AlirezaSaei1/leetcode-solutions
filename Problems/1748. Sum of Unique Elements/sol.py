class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        freq = Counter(nums)
        return sum(num for num, count in freq.items() if count == 1)