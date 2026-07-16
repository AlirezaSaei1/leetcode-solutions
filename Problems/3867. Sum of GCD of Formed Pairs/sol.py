class Solution:
    def gcdSum(self, nums: list[int]) -> int:
        n = len(nums)
        max_val = float('-inf')
        prefixGcd = [0] * n

        for i in range(n):
            max_val = max(max_val, nums[i])
            prefixGcd[i] = gcd(nums[i], max_val)
        
        prefixGcd.sort(reverse=True)
        answer = 0
        for i in range(n // 2):
            answer += gcd(prefixGcd[i], prefixGcd[~i])
            
        return answer