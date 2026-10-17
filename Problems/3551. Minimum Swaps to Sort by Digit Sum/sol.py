class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        def sum_digit(n):
            res = 0
            while n > 0:
                res += n % 10
                n //= 10
            return res

        sorted_nums = sorted(nums, key=lambda x: (sum_digit(x), x))
        target_map = {val: i for i, val in enumerate(sorted_nums)}

        n = len(nums)
        visited = [False] * n
        cycles = 0

        for i in range(n):
            if visited[i]:
                continue

            curr = i
            while not visited[curr]:
                visited[curr] = True
                curr = target_map[nums[curr]]

            cycles += 1

        return n - cycles