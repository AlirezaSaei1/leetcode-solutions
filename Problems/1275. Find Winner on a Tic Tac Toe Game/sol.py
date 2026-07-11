class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        rows = [0] * 3
        cols = [0] * 3
        diag = anti_diag = 0

        for i, (r, c) in enumerate(moves):
            player = 1 if i % 2 == 0 else -1
            rows[r] += player
            cols[c] += player
            if r == c:
                diag += player
            if r + c == 2:
                anti_diag += player
        
            if diag == 3 or anti_diag == 3 or rows[r] == 3 or cols[c] == 3:
                return 'A'
            if diag == -3 or anti_diag == -3 or rows[r] == -3 or cols[c] == -3:
                return 'B'
        
        return "Draw" if len(moves) == 9 else "Pending"
