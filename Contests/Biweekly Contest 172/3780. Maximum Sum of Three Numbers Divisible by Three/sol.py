class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        rem0 = []
        rem1 = []
        rem2 = []

        for num in nums:
            if num % 3 == 0:
                rem0.append(num)
            elif num % 3 == 1:
                rem1.append(num)
            else:
                rem2.append(num)

        rem0.sort()
        rem1.sort()
        rem2.sort()

        answer = 0
        
        n0 = len(rem0)
        if n0 > 2:
            res = rem0[n0-1] + rem0[n0-2] + rem0[n0-3]
            answer = max(answer, res)

        n1 = len(rem1)
        if n1 > 2:
            res = rem1[n1-1] + rem1[n1-2] + rem1[n1-3]
            answer = max(answer, res)

        n2 = len(rem2)
        if n2 > 2:
            res = rem2[n2-1] + rem2[n2-2] + rem2[n2-3]
            answer = max(answer, res)

        if n0 > 0 and n1 > 0 and n2 > 0:
            res = rem0[n0 - 1] + rem1[n1 - 1] + rem2[n2 - 1]
            answer = max(answer, res)
            
        return answer
            
            