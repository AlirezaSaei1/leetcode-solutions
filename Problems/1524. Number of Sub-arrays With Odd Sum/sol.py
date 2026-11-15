class Solution:
    def numOfSubarrays(self, arr: list[int]) -> int:
        MOD = 10**9 + 7
        even_count = 1
        odd_count = 0
        curr_parity = 0
        ans = 0

        for num in arr:
            curr_parity ^= num & 1
            if curr_parity == 1:
                ans += even_count
                odd_count += 1
            else:
                ans += odd_count
                even_count += 1

        return ans % MOD