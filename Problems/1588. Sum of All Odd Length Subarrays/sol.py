class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        n = len(arr)
        total = 0

        for i, val in enumerate(arr):
            left = i + 1
            right = n - i

            left_odd = left // 2
            left_even = left - left_odd

            right_odd = right // 2
            right_even = right - right_odd

            odd_count = left_odd * right_odd + left_even * right_even

            total += val * odd_count

        return total
