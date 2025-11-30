class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        self.result_matrix = image
        self.val = image[sr][sc]
        self.rows = len(image)
        self.cols = len(image[0]) if self.rows > 0 else 0

        def recursive_floodfill(i, j):
            if i < 0 or i >= self.rows or j < 0 or j >= self.cols:
                return

            if not self.result_matrix[i][j] == self.val or self.result_matrix[i][j] == color:
                return
            
            self.result_matrix[i][j] = color

            recursive_floodfill(i+1, j)
            recursive_floodfill(i, j+1)
            recursive_floodfill(i-1, j)
            recursive_floodfill(i, j-1)

        
        if self.result_matrix[sr][sc] == color:
            return self.result_matrix
        else:
            recursive_floodfill(sr, sc)
        
        return self.result_matrix
