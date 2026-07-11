class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        known = {0, firstPerson}
        
        meetings.sort(key=lambda x: x[2])
        
        grouped_meetings = []
        i = 0
        while i < len(meetings):
            current_time = meetings[i][2]
            current_group = []
            while i < len(meetings) and meetings[i][2] == current_time:
                current_group.append(meetings[i])
                i += 1
            grouped_meetings.append(current_group)
            
        for group in grouped_meetings:
            graph = defaultdict(list)
            people_in_this_time = set()
            
            for p1, p2, time in group:
                graph[p1].append(p2)
                graph[p2].append(p1)
                people_in_this_time.add(p1)
                people_in_this_time.add(p2)
            
            queue = deque()
            for p in people_in_this_time:
                if p in known:
                    queue.append(p)
            
            while queue:
                curr = queue.popleft()
                for neighbor in graph[curr]:
                    if neighbor not in known:
                        known.add(neighbor)
                        queue.append(neighbor)
                        
        return list(known)