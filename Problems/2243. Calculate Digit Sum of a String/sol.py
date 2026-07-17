class Solution:
    def digitSum(self, s: str, k: int) -> str:
        digits = [int(d) for d in s]

        while len(digits) > k:
            sums = []
            for i in range(0, len(digits), k):
                chunk_sum = sum(digits[i : i + k])
                sums.extend(int(d) for d in str(chunk_sum))
            digits = sums
        
        return ''.join(map(str, digits))

