class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        n = len(nums)
        indices = set()
        target_idx = [i for i in range(n) if nums[i]==key]

        for idx in target_idx:
            for i in range(max(0, idx - k), min(n, idx + k + 1)):
                indices.add(i)

        return sorted(indices)