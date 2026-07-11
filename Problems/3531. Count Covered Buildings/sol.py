class Solution:
    def countCoveredBuildings(self, n: int, buildings: List[List[int]]) -> int:
        xs = {}
        ys = {}

        for x, y in buildings:
            if x in xs:
                min_y, max_y = xs[x]
                xs[x] = (min(min_y, y), max(max_y, y))
            else:
                xs[x] = (y, y)

            if y in ys:
                min_x, max_x = ys[y]
                ys[y] = (min(min_x, x), max(max_x, x))
            else:
                ys[y] = (x, x)

        count = 0
        for x, y in buildings:
            min_y, max_y = xs[x]
            min_x, max_x = ys[y]
            if min_y < y < max_y and min_x < x < max_x:
                count += 1

        return count
