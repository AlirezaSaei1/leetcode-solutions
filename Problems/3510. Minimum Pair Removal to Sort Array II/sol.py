class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 1:
            return 0

        val = nums[:]
        alive = [True] * n
        prev = [-1] + list(range(n - 1))
        nxt = list(range(1, n)) + [-1]

        ver = [0] * n

        def bad_edge(i):
            j = nxt[i]
            return j != -1 and alive[i] and alive[j] and val[i] > val[j]

        bad = 0
        for i in range(n - 1):
            if val[i] > val[i + 1]:
                bad += 1
        if bad == 0:
            return 0

        pq = []
        for i in range(n - 1):
            heapq.heappush(pq, (val[i] + val[i + 1], i, ver[i]))

        ans = 0

        while bad > 0:
            while True:
                s, i, v = heapq.heappop(pq)
                j = nxt[i]
                if j == -1 or not alive[i] or not alive[j]:
                    continue
                if v != ver[i]:
                    continue
                if val[i] + val[j] != s:
                    continue
                break

            pi = prev[i]
            nj = nxt[j]

            for k in (pi, i, j):
                if k != -1 and bad_edge(k):
                    bad -= 1

            val[i] += val[j]
            alive[j] = False
            nxt[i] = nj
            if nj != -1:
                prev[nj] = i

            ver[i] += 1
            if pi != -1:
                ver[pi] += 1

            for k in (pi, i):
                if k != -1 and bad_edge(k):
                    bad += 1

            if pi != -1 and nxt[pi] != -1:
                heapq.heappush(pq, (val[pi] + val[nxt[pi]], pi, ver[pi]))
            if nxt[i] != -1:
                heapq.heappush(pq, (val[i] + val[nxt[i]], i, ver[i]))

            ans += 1

        return ans
