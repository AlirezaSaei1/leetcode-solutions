class Solution:
    def busiestServers(self, k: int, arrival: list[int], load: list[int]) -> list[int]:
        free_servers = SortedList(range(k))
        busy_servers = []
        requests_handled = [0] * k
        
        for i, (arr_time, dur) in enumerate(zip(arrival, load)):
            while busy_servers and busy_servers[0][0] <= arr_time:
                _, server_id = heapq.heappop(busy_servers)
                free_servers.add(server_id)
            
            if not free_servers:
                continue
            
            target = i % k
            idx = free_servers.bisect_left(target)
            
            if idx == len(free_servers):
                idx = 0
                
            assigned_server = free_servers[idx]
            free_servers.discard(assigned_server)
            
            requests_handled[assigned_server] += 1
            heapq.heappush(busy_servers, (arr_time + dur, assigned_server))
            
        max_handled = max(requests_handled)
        return [i for i, count in enumerate(requests_handled) if count == max_handled]