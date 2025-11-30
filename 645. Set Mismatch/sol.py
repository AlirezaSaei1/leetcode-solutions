class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        num_set = set()
        duplicate = -1
        total = 0

        for num in nums:
            if num in num_set:
                duplicate = num
            else:
                num_set.add(num)
                total += num

        expected_sum = n * (n + 1) // 2
        missing = expected_sum - total
        return [duplicate, missing]
