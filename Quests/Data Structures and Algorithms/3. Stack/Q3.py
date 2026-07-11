class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        durs = [0] * n
        stack = []
        prev = 0

        for log in logs:
            pid, st, t = log.split(':')
            pid = int(pid)
            t = int(t)

            if st == 'start':
                if stack:
                    durs[stack[-1]] += (t - prev)

                stack.append(pid)
                prev = t
            else:
                eid = stack.pop()
                durs[pid] += (t - prev + 1)
                prev = t + 1
        
        return durs