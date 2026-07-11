class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        def bsearch(row):
            n = len(row)
            left, right = 0, n - 1
            first_neg = n

            while left <= right:
                mid = (left + right) // 2

                if row[mid] < 0:
                    first_neg = mid
                    right = mid - 1
                else:
                    left = mid + 1

            return n - first_neg

        total_count = 0

        for row in grid:
            total_count += bsearch(row)
        
        return total_count
