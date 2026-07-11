class Solution:
    def sortByReflection(self, nums: List[int]) -> List[int]:
        final = []

        for num in nums:
            b = bin(num)[2:]
            b_new = b[::-1]
            int_new = int(b_new, 2)
            final.append((int_new, num))

        final.sort()
        return [b[1] for b in final]
        ©leetcode