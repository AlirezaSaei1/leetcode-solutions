class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        answer = 0
        nums.sort(key=abs)
        start, end = 0, len(nums) - 1
        flag = True

        while start <= end:
            if flag:
                answer += nums[end] ** 2
                end -= 1
                flag = not flag
            else:
                answer -= nums[start] ** 2
                start += 1
                flag = not flag
        
        return answer
            