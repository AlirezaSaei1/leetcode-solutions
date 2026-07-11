class Solution:
    def minOperations(self, s: str, k: int) -> int:
        n = len(s)
        z0 = s.count('0')
        if z0 == 0:
            return 0

        def build_dsu(parity: int):
            m = (n - parity) // 2 + 1
            parent = list(range(m + 1))

            def find(i: int) -> int:
                while parent[i] != i:
                    parent[i] = parent[parent[i]]
                    i = parent[i]
                return i

            def erase(i: int) -> None:
                i = find(i)
                if i < m:
                    parent[i] = find(i + 1)

            return m, parent, find, erase

        m0, parent0, find0, erase0 = build_dsu(0)
        m1, parent1, find1, erase1 = build_dsu(1)

        def idx_of(v: int) -> int:
            return v // 2

        dist = [-1] * (n + 1)
        q = deque()

        dist[z0] = 0
        q.append(z0)

        if z0 % 2 == 0:
            erase0(z0 // 2)
        else:
            erase1((z0 - 1) // 2)

        while q:
            z = q.popleft()
            d = dist[z]
            if z == 0:
                return d

            i_min = max(0, k - (n - z))
            i_max = min(k, z)
            if i_min > i_max:
                continue

            lo = z + k - 2 * i_max
            hi = z + k - 2 * i_min
            p = (z + k) & 1

            if p == 0:
                idx_lo = lo // 2
                idx_hi = hi // 2
                i = find0(idx_lo)
                while i <= idx_hi and i < m0:
                    nz = 2 * i
                    dist[nz] = d + 1
                    q.append(nz)
                    erase0(i)
                    i = find0(i)
            else:
                idx_lo = (lo - 1) // 2
                idx_hi = (hi - 1) // 2
                i = find1(idx_lo)
                while i <= idx_hi and i < m1:
                    nz = 2 * i + 1
                    dist[nz] = d + 1
                    q.append(nz)
                    erase1(i)
                    i = find1(i)

        return -1