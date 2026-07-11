class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapify(stones)
        while len(stones) > 1:
            max1 =  - heappop(stones)
            max2 =  - heappop(stones)

            if max1 != max2:
                heappush(stones, -(max1 - max2))
        
        if len(stones) == 1:
            return - heappop(stones)
        else:
            return 0