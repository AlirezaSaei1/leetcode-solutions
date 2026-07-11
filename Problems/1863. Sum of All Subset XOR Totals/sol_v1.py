class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        n = len(nums)

        def dfs(i: int, cur_xor: int) -> int:
            if i == n:
                return cur_xor
            return dfs(i + 1, cur_xor) + dfs(i + 1, cur_xor ^ nums[i])

        return dfs(0, 0)