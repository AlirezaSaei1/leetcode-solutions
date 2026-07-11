class Solution:
    def cellsInRange(self, s: str) -> List[str]:
        cells = []

        sc, sr = ord(s[0]) - ord('A'), int(s[1])
        ec, er = ord(s[3]) - ord('A'), int(s[4])

        for i in range(sc, ec + 1):
            col = chr(i + ord('A'))
            for j in range(sr, er + 1):
                cells.append(f'{col}{j}')
        
        return cells