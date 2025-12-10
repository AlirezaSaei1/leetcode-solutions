class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        start = None
        for i, num in enumerate(nums):
            if num == 1:
                if start is not None:
                    if i - start > k:
                        start = i
                    else:
                        return False
                else:
                    start = i
        return True