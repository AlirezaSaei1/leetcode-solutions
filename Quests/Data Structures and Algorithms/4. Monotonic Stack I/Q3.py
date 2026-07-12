class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        stack = []

        for i, height in enumerate(heights):
            start = i

            while stack and stack[-1][1] > height:
                previous_start, previous_height = stack.pop()

                width = i - previous_start
                area = previous_height * width
                max_area = max(max_area, area)

                start = previous_start
            
            stack.append((start, height))

        n = len(heights)

        while stack:
            start, height = stack.pop()
            width = n - start
            max_area = max(max_area, height * width)

        return max_area