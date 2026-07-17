class Solution:
    def gcdValues(self, nums: list[int], queries: list[int]) -> list[int]:
        max_num = max(nums)
        count_divisor = [0] * (max_num + 1)
        
        for num in nums:
            for i in range(1, isqrt(num) + 1):
                if num % i == 0:
                    count_divisor[i] += 1
                    if i*i != num:
                        count_divisor[num // i] += 1
        
        count_gcd_pair = [0] * (max_num + 1)
        for g in range(max_num, 0, -1):
            count = count_divisor[g]
            count_gcd_pair[g] = count * (count - 1) // 2

            for multiple in range(2 * g, max_num + 1, g):
                count_gcd_pair[g] -= count_gcd_pair[multiple]
        
        prefix_count_gcd_pair = list(accumulate(count_gcd_pair))
        return [bisect_right(prefix_count_gcd_pair, q) for q in queries]