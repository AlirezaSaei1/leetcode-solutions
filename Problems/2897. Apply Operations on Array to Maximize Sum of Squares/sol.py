class Solution:
    def maxSum(self, nums: List[int], k: int) -> int:
        MOD = 10**9 + 7
        bit_counts = [0] * 31

        for num in nums:
            for b in range(31):
                if (num >> b) & 1:
                    bit_counts[b] += 1
        
        total_sum = 0
        for _ in range(k):
            curr_num = 0
            for b in range(31):
                if bit_counts[b] > 0:
                    curr_num |= (1 << b)
                    bit_counts[b] -= 1

            total_sum = (total_sum + curr_num * curr_num) % MOD

        return total_sum