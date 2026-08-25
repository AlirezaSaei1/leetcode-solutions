class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        ns = set(nums)
        mult = 1

        while mult * k in ns:
           mult += 1
        
        return mult * k