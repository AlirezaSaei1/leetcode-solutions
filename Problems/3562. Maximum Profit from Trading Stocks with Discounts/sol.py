class Solution:
    def maxProfit(self, n: int, present: List[int], future: List[int],
                  hierarchy: List[List[int]], budget: int) -> int:
        children = defaultdict(list)
        for boss, emp in hierarchy:
            children[boss].append(emp)

        NEG = -10**15
        B = budget

        def merge(a: List[int], b: List[int]) -> List[int]:
            res = [NEG] * (B + 1)
            for i in range(B + 1):
                if a[i] == NEG:
                    continue

                for j in range(B - i + 1):
                    if b[j] == NEG:
                        continue
                    val = a[i] + b[j]
                    if val > res[i + j]:
                        res[i + j] = val
            return res

        def dfs(u: int):
            base = [NEG] * (B + 1)
            base[0] = 0

            skip_children = base[:]
            buy_children  = base[:]

            for v in children[u]:
                v0, v1 = dfs(v)
                skip_children = merge(skip_children, v0)
                buy_children  = merge(buy_children,  v1)

            dp0 = skip_children[:]
            dp1 = skip_children[:] 

            p_full = present[u - 1]
            p_disc = p_full // 2
            prof_full = future[u - 1] - p_full
            prof_disc = future[u - 1] - p_disc

            for c in range(B - p_full + 1):
                if buy_children[c] == NEG:
                    continue
                cand = buy_children[c] + prof_full
                if cand > dp0[c + p_full]:
                    dp0[c + p_full] = cand

            for c in range(B - p_disc + 1):
                if buy_children[c] == NEG:
                    continue
                cand = buy_children[c] + prof_disc
                if cand > dp1[c + p_disc]:
                    dp1[c + p_disc] = cand

            return dp0, dp1

        root_dp0, _ = dfs(1)

        return max(root_dp0)
