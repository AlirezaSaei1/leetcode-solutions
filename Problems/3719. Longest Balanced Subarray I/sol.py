class Solution:
    def longestBalanced(self, nums: List[int]) -> int:
        n = len(nums)
        answer = 0

        for i in range(n):
            seen_odd = set()
            seen_even = set()

            for j in range(i, n):
                if nums[j] % 2 == 0:
                    seen_even.add(nums[j])
                else:
                    seen_odd.add(nums[j])
                
                if len(seen_even) == len(seen_odd):
                    answer = max(answer, j - i + 1)
        
        return answer