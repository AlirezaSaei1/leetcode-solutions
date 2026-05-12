class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        ans = []
        for num in nums:
            for char in str(num):
                ans.append(int(char))
        return ans