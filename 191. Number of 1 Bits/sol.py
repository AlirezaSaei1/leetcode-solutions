class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        number = bin(n)
        for i in number:
            if i == '1':
                count += 1
        return count
