class Solution:
    def findLHS(self, nums: List[int]) -> int:
        counter = Counter(nums)
        longest = 0

        for num in counter:
            if num+1 in counter.keys():
                length = counter[num] + counter[num+1]
                longest = max(longest, length)
        
        return longest
            