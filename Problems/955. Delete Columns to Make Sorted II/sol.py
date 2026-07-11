class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        n = len(strs)
        m = len(strs[0])
        sorted_pairs = [False] * (n - 1)
        deletions = 0
        
        for col in range(m):
            delete_this_col = False
            
            for i in range(n - 1):
                if sorted_pairs[i]:
                    continue

                if strs[i][col] > strs[i+1][col]:
                    delete_this_col = True
                    break
            
            if delete_this_col:
                deletions += 1
            else:
                for i in range(n - 1):
                    if strs[i][col] < strs[i+1][col]:
                        sorted_pairs[i] = True
                        
        return deletions