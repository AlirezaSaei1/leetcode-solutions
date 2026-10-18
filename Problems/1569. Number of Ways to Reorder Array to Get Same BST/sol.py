class Solution:
    def numOfWays(self, nums: list[int]) -> int:
        MOD = 10**9 + 7

        def count(arr: list[int]) -> int:
            if len(arr) <= 2:
                return 1

            root = arr[0]
            left = [x for x in arr[1:] if x < root]
            right = [x for x in arr[1:] if x > root]

            interleave_ways = math.comb(len(left) + len(right), len(left)) % MOD

            return (interleave_ways * count(left) * count(right)) % MOD

        return (count(nums) - 1) % MOD