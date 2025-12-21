class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        n = len(strs)
        if n == 1: 
            return 0
        
        m = len(strs[0])
        is_sorted = [False] * (n - 1)
        deletions = 0
        
        for col in range(m):
            potential_updates = []
            bad_column = False
            
            for i in range(n - 1):
                if is_sorted[i]:
                    continue
                
                s1, s2 = strs[i][col], strs[i+1][col]
                
                if s1 > s2:
                    bad_column = True
                    deletions += 1
                    break
                elif s1 < s2:
                    potential_updates.append(i)
            
            if not bad_column:
                for i in potential_updates:
                    is_sorted[i] = True
                    
        return deletions