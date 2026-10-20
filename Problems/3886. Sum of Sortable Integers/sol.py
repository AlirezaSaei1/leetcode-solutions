class Solution:
    def sortableIntegers(self, nums: list[int]) -> int:
        n = len(nums)
        target = sorted(nums)

        divisors = []
        d = 1
        while d * d <= n:
            if n % d == 0:
                divisors.append(d)
                if d * d != n:
                    divisors.append(n // d)
            d += 1

        def can_rotate_to_target(start: int, k: int) -> bool:
            first_decrease = -1
            for j in range(k - 1):
                if nums[start + j] > nums[start + j + 1]:
                    first_decrease = j
                    break

            if first_decrease == -1:
                return nums[start : start + k] == target[start : start + k]

            offset = first_decrease + 1
            for j in range(k):
                if nums[start + (offset + j) % k] != target[start + j]:
                    return False

            return True

        ans = 0
        for k in divisors:
            is_sortable = True
            for i in range(0, n, k):
                if not can_rotate_to_target(i, k):
                    is_sortable = False
                    break

            if is_sortable:
                ans += k

        return ans