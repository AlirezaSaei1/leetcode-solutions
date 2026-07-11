class Solution:
    def checkZeroOnes(self, s: str) -> bool:
        longest_0, longest_1 = 0, 0
        cur_0, cur_1 = 0, 0

        for char in s:
            if char == '1':
                cur_1 += 1
                cur_0 = 0
            else:
                cur_0 += 1
                cur_1 = 0
            
            longest_1 = max(longest_1, cur_1)
            longest_0 = max(longest_0, cur_0)

        return longest_1 > longest_0