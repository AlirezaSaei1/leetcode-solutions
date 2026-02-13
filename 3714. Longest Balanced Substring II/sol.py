class Solution:
    def longestBalanced(self, s: str) -> int:
        sm = s
        n = len(sm)
        if n == 0:
            return 0

        seen = {(0, 0): -1}
        ca = cb = cc = 0
        best = 0
        for i, ch in enumerate(sm):
            if ch == 'a':
                ca += 1
            elif ch == 'b':
                cb += 1
            else:
                cc += 1
            key = (ca - cb, ca - cc)
            if key in seen:
                best = max(best, i - seen[key])
            else:
                seen[key] = i

        pairs = [('a', 'b', 'c'), ('a', 'c', 'b'), ('b', 'c', 'a')]
        for x, y, forbidden in pairs:
            start = 0
            while start < n:
                if sm[start] == forbidden:
                    start += 1
                    continue
                end = start
                while end < n and sm[end] != forbidden:
                    end += 1

                diff_map = {0: -1}
                diff = 0
                seg_best = 0
                run_char = None
                run_len = 0

                for idx in range(start, end):
                    ch = sm[idx]
                    if ch == x:
                        diff += 1
                    elif ch == y:
                        diff -= 1
                    rel = idx - start
                    if diff in diff_map:
                        seg_best = max(seg_best, rel - diff_map[diff])
                    else:
                        diff_map[diff] = rel

                    if ch == run_char:
                        run_len += 1
                    else:
                        run_char = ch
                        run_len = 1
                    seg_best = max(seg_best, run_len)

                best = max(best, seg_best)
                start = end

        return best