class Solution:
    def minimumCost(self, nums: List[int], k: int, dist: int) -> int:
        n = len(nums)
        t = k - 2
        INF = 10**30

        small = []
        large = []
        delayed = defaultdict(int)

        in_small = [False] * n
        size_small = 0
        size_large = 0
        sum_small = 0

        def prune_small():
            nonlocal size_small, sum_small
            while small:
                val_neg, idx = small[0]
                if delayed[idx]:
                    heapq.heappop(small)
                    delayed[idx] -= 1
                    if delayed[idx] == 0:
                        del delayed[idx]
                else:
                    break

        def prune_large():
            while large:
                val, idx = large[0]
                if delayed[idx]:
                    heapq.heappop(large)
                    delayed[idx] -= 1
                    if delayed[idx] == 0:
                        del delayed[idx]
                else:
                    break

        def rebalance():
            nonlocal size_small, size_large, sum_small
            prune_small()
            prune_large()

            while size_small > t:
                prune_small()
                val_neg, idx = heapq.heappop(small)
                val = -val_neg
                in_small[idx] = False
                sum_small -= val
                size_small -= 1
                heapq.heappush(large, (val, idx))
                size_large += 1

            while size_small < t and size_large > 0:
                prune_large()
                val, idx = heapq.heappop(large)
                in_small[idx] = True
                sum_small += val
                size_large -= 1
                heapq.heappush(small, (-val, idx))
                size_small += 1

            prune_small()
            prune_large()
            while size_small > 0 and size_large > 0:
                max_small = -small[0][0]
                min_large = large[0][0]
                if max_small <= min_large:
                    break

                valS_neg, idxS = heapq.heappop(small)
                valS = -valS_neg
                valL, idxL = heapq.heappop(large)

                in_small[idxS] = False
                in_small[idxL] = True
                sum_small += valL - valS

                heapq.heappush(small, (-valL, idxL))
                heapq.heappush(large, (valS, idxS))

        def add(idx: int):
            nonlocal size_small, size_large, sum_small
            val = nums[idx]

            heapq.heappush(large, (val, idx))
            in_small[idx] = False
            size_large += 1
            rebalance()

        def remove(idx: int):
            nonlocal size_small, size_large, sum_small
            delayed[idx] += 1
            if in_small[idx]:
                in_small[idx] = False
                size_small -= 1
                sum_small -= nums[idx]
            else:
                size_large -= 1
            rebalance()

        l = 2
        r = min(1 + dist, n - 1)
        for idx in range(l, r + 1):
            add(idx)

        ans = INF

        for i in range(1, n):
            # window for this i is [i+1 .. min(i+dist, n-1)]
            window_size = max(0, min(i + dist, n - 1) - (i + 1) + 1)
            if window_size >= t and size_small == t:
                ans = min(ans, nums[0] + nums[i] + sum_small)

            if i == n - 1:
                break
            old_left = i + 1
            new_right = i + dist + 1
            if old_left <= n - 1:
                remove(old_left)
            if new_right <= n - 1:
                add(new_right)

        return ans
