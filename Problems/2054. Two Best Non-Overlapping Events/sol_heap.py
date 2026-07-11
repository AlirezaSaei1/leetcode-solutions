class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        events.sort()
        
        min_heap = []
        max_val = 0
        ans = 0
        
        for start, end, val in events:
            while min_heap and min_heap[0][0] < start:
                _, v = heapq.heappop(min_heap)
                max_val = max(max_val, v)
            
            ans = max(ans, val + max_val)
            
            heapq.heappush(min_heap, (end, val))
            
        return ans