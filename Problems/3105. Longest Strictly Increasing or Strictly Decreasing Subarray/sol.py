class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        leng = 1
        answer = 1
        inc = True
        prev = nums[0]

        for i in range(1, len(nums)):
            if nums[i] > prev:
                if inc:
                    leng += 1
                else:
                    inc = not inc
                    leng = 2
            elif nums[i] < prev:
                if not inc:
                    leng += 1
                else:
                    inc = not inc
                    leng = 2
            else:
                leng = 1

            answer = max(answer, leng)
            prev = nums[i]

        return answer