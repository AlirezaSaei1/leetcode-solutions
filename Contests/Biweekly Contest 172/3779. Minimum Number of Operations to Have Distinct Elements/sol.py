class Solution:
    def minOperations(self, nums: List[int]) -> int:
        seen = set()
        n = len(nums)
        i = n - 1

        while i >= 0:
            if nums[i] in seen:
                break
            else:
                seen.add(nums[i])
                i -= 1


        answer = 0
        while i + 1 > 0:
            i -= 3
            answer += 1

        return answer