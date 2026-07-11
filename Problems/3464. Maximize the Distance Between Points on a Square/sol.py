class Solution:
    def maxDistance(self, side: int, points: List[List[int]], k: int) -> int:
        def get_dist(p):
            x, y = p
            if y == 0: return x
            if x == side: return side + y
            if y == side: return 2 * side + (side - x)
            return 3 * side + (side - y)

        dists = sorted([get_dist(p) for p in points])
        n = len(dists)
        total_len = 4 * side

        def check(mid):
            for start_idx in range(n):
                count = 1
                last_pos = dists[start_idx]
                curr_idx = start_idx
                
                limit = dists[start_idx] + total_len - mid
                
                for _ in range(k - 1):
                    target = last_pos + mid
                    if target > limit:
                        count = -1
                        break
                    
                    idx = bisect_left(dists, target, lo=curr_idx + 1)
                    if idx == n:
                        count = -1
                        break
                    
                    last_pos = dists[idx]
                    curr_idx = idx
                
                if count != -1 and last_pos <= limit:
                    return True
                
                if start_idx > 0 and dists[start_idx] > dists[0] + mid:
                    break
            return False

        low, high = 1, total_len // k
        ans = 0
        while low <= high:
            mid = (low + high) // 2
            if check(mid):
                ans = mid
                low = mid + 1
            else:
                high = mid - 1
        return ans