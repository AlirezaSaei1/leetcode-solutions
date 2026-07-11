class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        rows = len(img)
        cols = len(img[0])
        output = [[0 for _ in range(cols)] for _ in range(rows)]


        for i in range(rows):
            for j in range(cols):
                total = 0
                count = 0
                for dx in [-1, 0, 1]:
                    for dy in [-1, 0, 1]:
                        in_x, in_y = i + dx, j + dy
                        if 0 <= in_x < rows and 0 <= in_y < cols:
                            total += img[in_x][in_y]
                            count += 1
                
                output[i][j] = total // count
        return output