class Solution:
    def countMentions(self, numberOfUsers: int, events: List[List[str]]) -> List[int]:
        online = set(range(numberOfUsers))
        offline = set()
        mentions = [0] * numberOfUsers

        events.sort(key=lambda x: (int(x[1]), 0 if x[0] == "OFFLINE" else 1))
        heap = []

        for event in events:
            typ, t_str, data = event
            t = int(t_str)

            while heap and heap[0][0] <= t:
                _, u = heapq.heappop(heap)
                offline.remove(u)
                online.add(u)

            if typ == "OFFLINE":
                u = int(data)
                if u in online:
                    online.remove(u)
                    offline.add(u)
                    heapq.heappush(heap, (t + 60, u))
            else:
                if data == "ALL":
                    for u in range(numberOfUsers):
                        mentions[u] += 1

                elif data == "HERE":
                    for u in online:
                        mentions[u] += 1

                else:
                    for token in data.split():
                        u = int(token[2:])
                        mentions[u] += 1

        return mentions



