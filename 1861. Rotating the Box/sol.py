class Solution:
    def rotateTheBox(self, boxGrid: List[List[str]]) -> List[List[str]]:
        m = len(boxGrid)
        n = len(boxGrid[0])
        
        # 1. Apply gravity within each row
        for row in boxGrid:
            empty_pos = n - 1
            for col in range(n - 1, -1, -1):
                if row[col] == "#":
                    # Move stone to the rightmost empty position
                    row[col], row[empty_pos] = ".", "#"
                    empty_pos -= 1
                elif row[col] == "*":
                    # Obstacle resets the landing spot for stones above it
                    empty_pos = col - 1
                    
        # 2. Rotate the box 90 degrees clockwise
        # Original (m x n) -> Rotated (n x m)
        rotated_box = [["" for _ in range(m)] for _ in range(n)]
        for r in range(m):
            for c in range(n):
                rotated_box[c][m - 1 - r] = boxGrid[r][c]
                
        return rotated_box