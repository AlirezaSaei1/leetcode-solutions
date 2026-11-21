class Solution:
    def findSubtreeSizes(self, parent: List[int], s: str) -> List[int]:
        n = len(parent)
        adj = [[] for _ in range(n)]
        for i in range(1, n):
            adj[parent[i]].append(i)

        sz = [1] * n
        last_seen = [-1] * 26
        stack = [(0, False, -1)]

        while stack:
            u, exiting, prev = stack.pop()
            c = ord(s[u]) - 97

            if not exiting:
                prev_anc = last_seen[c]
                last_seen[c] = u
                stack.append((u, True, prev_anc))
                for v in adj[u]:
                    stack.append((v, False, -1))
            else:
                last_seen[c] = prev
                target = prev if prev != -1 else parent[u]
                if target != -1:
                    sz[target] += sz[u]

        return sz