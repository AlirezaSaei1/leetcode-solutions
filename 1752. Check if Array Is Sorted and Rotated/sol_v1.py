class Solution:
    def check(self, nums: List[int]) -> bool:
        n = len(nums)

        for i in range(n):
            ok = True

            # check nums[i..n-1]
            prev = nums[i]
            for j in range(i + 1, n):
                if prev > nums[j]:
                    ok = False
                    break
                prev = nums[j]

            if not ok:
                continue

            # check nums[0..i-1]
            prev = nums[0]
            for j in range(1, i):
                if prev > nums[j]:
                    ok = False
                    break
                prev = nums[j]

            if ok and (i == 0 or nums[n - 1] <= nums[0]):
                return True

        return False
