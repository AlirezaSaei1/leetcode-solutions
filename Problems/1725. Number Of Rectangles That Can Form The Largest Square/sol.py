class Solution:
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        max_len, max_count = 0, 0

        for x, y in rectangles:
            k = min(x, y)
            
            if k > max_len:
                max_len = k
                max_count = 0

            if k == max_len:
                max_count += 1
            
        return max_count
