# Pruning

class Solution:
    def largestSquareArea(self, bottomLeft: List[List[int]], topRight: List[List[int]]) -> int:
        n = len(bottomLeft)
        rects = []

        for i in range(n):
            w = topRight[i][0] - bottomLeft[i][0]
            h = topRight[i][1] - bottomLeft[i][1]
            rects.append((min(w, h), i))

        rects.sort(reverse=True)  # big first
        max_side = 0

        for idx1 in range(n):
            if rects[idx1][0] <= max_side:
                break
            i = rects[idx1][1]

            for idx2 in range(idx1 + 1, n):
                if rects[idx2][0] <= max_side:
                    break
                j = rects[idx2][1]

                left = max(bottomLeft[i][0], bottomLeft[j][0])
                right = min(topRight[i][0], topRight[j][0])
                bottom = max(bottomLeft[i][1], bottomLeft[j][1])
                top = min(topRight[i][1], topRight[j][1])

                if right > left and top > bottom:
                    side = min(right - left, top - bottom)
                    max_side = max(max_side, side)

        return max_side * max_side
