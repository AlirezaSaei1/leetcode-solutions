class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        ops = []
        cur = 1

        for i in range(len(target)):
            while target[i] != cur:
                ops.append('Push')
                ops.append('Pop')
                cur += 1
            
            if target[i] == cur:
                ops.append('Push')
            
            cur += 1
        
        return ops