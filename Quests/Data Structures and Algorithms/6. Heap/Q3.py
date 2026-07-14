class Solution:
    def isPossible(self, target: List[int]) -> bool:
        if len(target) == 1:
            return target[0] == 1
        
        total_sum = sum(target)
        max_heap = [-x for x in target]
        heapq.heapify(max_heap)
        
        while -max_heap[0] > 1:
            m = -heapq.heappop(max_heap)
            rest = total_sum - m
            
            if rest == 0 or m <= rest:
                return False
            
            prev = m % rest

            if prev == 0 and rest > 1:
                return False
                
            total_sum = rest + prev
            heapq.heappush(max_heap, -prev)
            
        return True