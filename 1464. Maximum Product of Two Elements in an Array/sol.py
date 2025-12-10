class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        first = second = float('-inf')
        for num in nums:
            if num >= first:
                second = first
                first = num
            elif first > num > second:
                second = num

        return (first - 1) * (second - 1)