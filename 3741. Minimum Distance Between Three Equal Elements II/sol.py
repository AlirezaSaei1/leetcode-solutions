class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        mp = defaultdict(list)

        for idx, val in enumerate(nums):
            mp[val].append(idx)
        
        answer = float('inf')

        for dists in mp.values():
            n = len(dists)
            if n < 3:
                continue
            for m in range(n-2):
                answer = min(answer, dists[m+2] - dists[m])
        
        return answer * 2 if answer != float('inf') else -1