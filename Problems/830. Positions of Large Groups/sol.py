class Solution:
    def largeGroupPositions(self, s: str) -> List[List[int]]:
        start = -1
        end = -1
        group = None
        large_groups = []
        i = 0
        while i < len(s):
            if not group:
                group = s[i]
                start = i
                end = i
                i += 1
            else:
                if group == s[i]:
                    end = i
                    i+= 1
                else:
                    if end - start >= 2:
                        large_groups.append([start, end])
                        
                    group = None
                    
        if group and end - start >= 2:
            large_groups.append([start, end])
            
        return large_groups
