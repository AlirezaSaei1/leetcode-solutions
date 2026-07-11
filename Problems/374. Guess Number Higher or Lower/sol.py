class Solution:
    def guessNumber(self, n: int) -> int:
        left = 1
        right = n

        while left <= right:
            mid = left + (right - left) // 2
            hint = guess(mid)

            if hint == 0:
                return mid
            elif hint == 1:
                left = mid + 1
            else:
                right = mid - 1
