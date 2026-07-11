class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        arr = sorted((num, i) for i, num in enumerate(nums))
        res = [0] * len(nums)
        prev = -1

        for rank, (num, idx) in enumerate(arr):
            if rank == 0 or num != arr[rank - 1][0]:
                prev = rank
            res[idx] = prev
        
        return res