class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        n = len(nums)
        res = []
        key_indices = [i for i, x in enumerate(nums) if x == key]
        
        curr_key = 0
        for i in range(n):
            while curr_key < len(key_indices) and key_indices[curr_key] < i - k:
                curr_key += 1

            if curr_key < len(key_indices) and abs(key_indices[curr_key] - i) <= k:
                res.append(i)
        
        return res