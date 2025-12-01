class Solution:
    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        def can_run(t: int) -> bool:
            total = 0
            for b in batteries:
                total += min(b, t)
                if total >= n * t:
                    return True
            return total >= n * t

        
        left = 0
        right = sum(batteries) // n

        while left < right:
            mid = (left + right + 1) // 2

            if can_run(mid):
                left = mid
            else:
                right = mid - 1
        
        return left