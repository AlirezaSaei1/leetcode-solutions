class Solution:
    def assignTasks(self, servers: list[int], tasks: list[int]) -> list[int]:
        free_servers = []
        for i, weight in enumerate(servers):
            heapq.heappush(free_servers, (weight, i))
            
        busy_servers = []
        ans = []
        
        for j, duration in enumerate(tasks):
            while busy_servers and busy_servers[0][0] <= j:
                free_time, weight, index = heapq.heappop(busy_servers)
                heapq.heappush(free_servers, (weight, index))
                
            if free_servers:
                weight, index = heapq.heappop(free_servers)
                ans.append(index)
                heapq.heappush(busy_servers, (j + duration, weight, index))
            else:
                free_time, weight, index = heapq.heappop(busy_servers)
                ans.append(index)
                heapq.heappush(busy_servers, (free_time + duration, weight, index))
                
        return ans