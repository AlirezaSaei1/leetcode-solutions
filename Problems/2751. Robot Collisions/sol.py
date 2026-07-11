class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        n = len(positions)
        robots = []
        for i in range(n):
            robots.append([positions[i], healths[i], directions[i], i])
        
        robots.sort()
        
        stack = []
        
        for i in range(n):
            curr = robots[i]
            
            if curr[2] == 'R':
                stack.append(curr)
            else:
                while stack and stack[-1][2] == 'R' and curr[1] > 0:
                    top = stack[-1]
                    
                    if curr[1] > top[1]:
                        stack.pop()
                        curr[1] -= 1
                    elif curr[1] < top[1]:
                        top[1] -= 1
                        curr[1] = 0
                    else:
                        stack.pop()
                        curr[1] = 0
                
                if curr[1] > 0:
                    stack.append(curr)
        
        stack.sort(key=lambda x: x[3])
        
        return [robot[1] for robot in stack]