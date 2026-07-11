class Solution:
    def minLength(self, nums: List[int], k: int) -> int:
        n = len(nums)
        left, total = 0, 0
        answer = float('inf')
        s = {}
        
        for right in range(n):
            num = nums[right]
            if num not in s:
                s[num] = 0
            if s[num] == 0:
                total += num
            s[nums[right]] += 1

            while total >= k:
                cur_len = right - left + 1
                if cur_len < answer:
                    answer = cur_len

                s[nums[left]] -= 1
                if s[nums[left]] == 0:
                    total -= nums[left]
                left += 1

        if answer == float('inf'):
            return -1
        return answer