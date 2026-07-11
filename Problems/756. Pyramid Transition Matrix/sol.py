class Solution:
    def pyramidTransition(self, bottom: str, allowed: List[str]) -> bool:
        mp = defaultdict(list)
        for a, b, c in allowed:
            mp[a + b].append(c)

        memo = {}

        def dfs(row):
            if row in memo:
                return memo[row]

            if len(row) == 1:
                return True

            def backtrack(i, path):
                if i == len(row) - 1:
                    return dfs("".join(path))

                key = row[i:i+2]
                if key not in mp:
                    return False

                for ch in mp[key]:
                    path.append(ch)
                    if backtrack(i + 1, path):
                        return True
                    path.pop()

                return False

            memo[row] = backtrack(0, [])
            return memo[row]

        return dfs(bottom)
