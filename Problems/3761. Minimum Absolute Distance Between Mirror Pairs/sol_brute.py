class Solution:
    def minMirrorPairDistance(self, nums: List[int]) -> int:
        n = len(nums)
        answer = float('inf')
        rev_nums = [int(str(num)[::-1]) for num in nums]

        for i in range(n):
            for j in range(i+1, n):
                if rev_nums[i] == nums[j]:
                    answer = min(answer, j - i)
        
        return answer if answer != float('inf') else -1

