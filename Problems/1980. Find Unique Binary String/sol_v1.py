class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        n = len(nums[0])
        rng = set(range(2 ** n))
        numbers = set([int(x, 2) for x in nums])
        
        diff = rng - numbers
        answer = bin(diff.pop())[2:]
        ln = len(answer)
        return '0' * (n - ln) + answer
