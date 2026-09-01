class Solution:
    def minMoves(self, classroom: List[str], energy: int) -> int:
        m, n = len(classroom), len(classroom[0])
        start_r, start_c = -1, -1
        litter_coords = []

        for r in range(m):
            for c in range(n):
                if classroom[r][c] == 'S':
                    start_r, start_c = r, c
                elif classroom[r][c] == 'L':
                    litter_coords.append((r, c))

        total_litter = len(litter_coords)
        full_mask = (1 << total_litter) - 1

        litter_map = {pos: i for i, pos in enumerate(litter_coords)}

        queue = deque([(start_r, start_c, 0, energy, 0)])
        best_energy = [[[-1] * (1 << total_litter) for _ in range(n)] for _ in range(m)]

        best_energy[start_r][start_c][0] = energy

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        while queue:
            r, c, mask, e, steps = queue.popleft()

            if mask == full_mask:
                return steps

            if e == 0:
                continue

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if 0 <= nr < m and 0 <= nc < n and classroom[nr][nc] != 'X':
                    next_e = e - 1
                    next_mask = mask
                    cell = classroom[nr][nc]

                    if cell == 'L':
                        bit = litter_map[(nr, nc)]
                        next_mask |= (1 << bit)
                    elif cell == 'R':
                        next_e = energy

                    if next_e > best_energy[nr][nc][next_mask]:
                        best_energy[nr][nc][next_mask] = next_e
                        queue.append((nr, nc, next_mask, next_e, steps + 1))

        return -1