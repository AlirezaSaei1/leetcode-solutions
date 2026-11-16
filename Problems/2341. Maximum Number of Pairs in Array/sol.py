class Solution:
    def numberOfPairs(self, nums: list[int]) -> list[int]:
        freq = Counter(nums)
        num_pairs = 0
        num_left = 0

        for key in freq:
            count = freq[key]
            num_pairs += (count // 2)
            if count % 2 == 1:
                num_left += 1
        
        return [num_pairs, num_left]
