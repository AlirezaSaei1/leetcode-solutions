class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        attack_count = 0
        rook_row, rook_col = 0, 0
        
        # find rook
        for i in range(8):
            for j in range(8):
                if board[i][j] == "R":
                    rook_row, rook_col = i, j
                    break
        
        # up
        ri = rook_row - 1
        while ri >= 0:
            if board[ri][rook_col] == 'B':
                break
            if board[ri][rook_col] == 'p':
                attack_count += 1
                break
            ri -= 1

        # down
        ri = rook_row + 1
        while ri < 8:
            if board[ri][rook_col] == 'B':
                break
            if board[ri][rook_col] == 'p':
                attack_count += 1
                break
            ri += 1

        # right
        rc = rook_col + 1
        while rc < 8:
            if board[rook_row][rc] == 'B':
                break
            if board[rook_row][rc] == 'p':
                attack_count += 1
                break
            rc += 1

        # left
        rc = rook_col - 1
        while rc >= 0:
            if board[rook_row][rc] == 'B':
                break
            if board[rook_row][rc] == 'p':
                attack_count += 1
                break
            rc -= 1

        return attack_count
