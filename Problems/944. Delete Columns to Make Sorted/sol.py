class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        n = len(strs)
        m = len(strs[0])
        del_count = 0

        for i in range(m):
            for j in range(1, n):
                if strs[j-1][i] > strs[j][i]:
                    del_count += 1
                    break
        
        return del_count
            
