class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        first_pos = {}
        last_pos = {}
        count = {}

        for i, num in enumerate(nums):
            if num not in count:
                first_pos[num] = i
                count[num] = 1
            else:
                count[num] += 1
            last_pos[num] = i
        
        degree = max(count.values())
        min_len = len(nums)

        for num, freq in count.items():
            cur_len = 0
            if freq == degree:
                cur_len = last_pos[num] - first_pos[num] + 1
            
                if cur_len < min_len:
                    min_len = cur_len
        
        return min_len

            