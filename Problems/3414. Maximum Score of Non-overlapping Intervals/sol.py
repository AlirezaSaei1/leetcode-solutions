class Solution:
    def maximumWeight(self, intervals: List[List[int]]) -> List[int]:
        n = len(intervals)
        
        arr = [(l, r, w, i) for i, (l, r, w) in enumerate(intervals)]
        arr.sort(key=lambda x: x[0])
        
        starts = [x[0] for x in arr]
        next_pos = [bisect_right(starts, arr[i][1]) for i in range(n)]

        @lru_cache(None)
        def dp(i: int, k: int):
            if i >= n or k == 0:
                return (0, ())

            res_weight, res_indices = dp(i + 1, k)

            nxt = next_pos[i]
            take_weight, take_indices = dp(nxt, k - 1)
            new_weight = arr[i][2] + take_weight
            new_indices = tuple(sorted((arr[i][3],) + take_indices))

            if new_weight > res_weight:
                res_weight, res_indices = new_weight, new_indices
            elif new_weight == res_weight:
                if new_indices < res_indices:
                    res_indices = new_indices

            return (res_weight, res_indices)

        best_weight, best_indices = dp(0, 4)
        return list(best_indices)