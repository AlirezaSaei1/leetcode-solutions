class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        def is_non_decreasing(arr):
            return all(arr[i] <= arr[i+1] for i in range(len(arr) - 1))

        arr = nums[:]
        ops = 0

        while not is_non_decreasing(arr):
            i = min(
                range(len(arr) - 1),
                key=lambda j: arr[j] + arr[j + 1]
            )

            arr[i:i+2] = [arr[i] + arr[i+1]]
            ops += 1

        return ops
