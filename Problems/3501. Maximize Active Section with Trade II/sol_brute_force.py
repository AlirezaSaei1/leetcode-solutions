class Solution:
    def maxActiveSectionsAfterTrade(self, s: str, queries: list[list[int]]) -> list[int]:
        n, m = len(s), len(queries)
        cnt1 = s.count("1")

        left = [1] * n
        right = [1] * n
        for i in range(n):
            left[i] = left[i - 1] + 1 if i > 0 and s[i - 1] == s[i] else 1
        for i in range(n - 1, -1, -1):
            right[i] = right[i + 1] + 1 if i < n - 1 and s[i + 1] == s[i] else 1

        ans = [-1] * m
        block_size = isqrt(n) + 1

        longQueries = []

        def brute_force(l, r) -> int:
            i = l
            best = 0
            prev = -inf

            while i <= r:
                start = i
                while i <= r and s[i] == s[start]:
                    i += 1
                if s[start] == "0":
                    cur = i - start
                    best = prev + cur if prev + cur > best else best
                    prev = cur
            return best

        for i, (l, r) in enumerate(queries):
            if r - l + 1 > block_size:
                longQueries.append((l // block_size, l, r, i))
            else:
                ans[i] = cnt1 + brute_force(l, r)

        longQueries.sort(key=lambda q: (q[0], q[2]))
        subZeroBlocks = deque()

        for i, (bid, l, r, qid) in enumerate(longQueries):
            if i == 0 or bid > longQueries[i - 1][0]:
                L = (bid + 1) * block_size - 1
                R = (bid + 1) * block_size
                subZeroBlocks.clear()
                bestGain = 0

            while R <= r:
                sz = min(r - R + 1, right[R])
                if s[R] == "0":
                    if subZeroBlocks and s[R - 1] == "0":
                        subZeroBlocks[-1] += sz
                    else:
                        subZeroBlocks.append(sz)
                    if len(subZeroBlocks) >= 2:
                        bestGain = max(subZeroBlocks[-1] + subZeroBlocks[-2], bestGain)
                R += sz

            tmp_bestGain = bestGain
            tmp_firstValue = subZeroBlocks[0] if subZeroBlocks else None
            cnt = 0

            while L >= l:
                sz = min(L - l + 1, left[L])
                if s[L] == "0":
                    if subZeroBlocks and s[L + 1] == "0":
                        subZeroBlocks[0] += sz
                    else:
                        subZeroBlocks.appendleft(sz)
                        cnt += 1
                    if len(subZeroBlocks) >= 2:
                        bestGain = max(subZeroBlocks[0] + subZeroBlocks[1], bestGain)
                L -= sz

            ans[qid] = bestGain + cnt1

            L = (bid + 1) * block_size - 1
            bestGain = tmp_bestGain

            for _ in range(cnt):
                subZeroBlocks.popleft()
            if tmp_firstValue is not None and subZeroBlocks:
                subZeroBlocks[0] = tmp_firstValue

        return ans