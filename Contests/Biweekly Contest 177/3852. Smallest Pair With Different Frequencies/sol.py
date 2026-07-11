class Solution:
    def minDistinctFreqPair(self, nums: list[int]) -> list[int]:
        nums.sort()
        x = nums[0]
        n = len(nums)

        if n < 2:
            return [-1, -1]

        freq = Counter(nums)
        sorted_keys = sorted(freq.keys())

        for i in range(len(sorted_keys)):
            for j in range(i + 1, len(sorted_keys)):
                if freq[sorted_keys[i]] != freq[sorted_keys[j]]:
                    return [sorted_keys[i], sorted_keys[j]]

        return [-1, -1]