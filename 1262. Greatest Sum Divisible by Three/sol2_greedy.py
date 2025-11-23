class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        total = sum(nums)
        r = total % 3
        
        if r == 0:
            return total
        
        INF = math.inf
        
        m1_1, m1_2 = INF, INF
        m2_1, m2_2 = INF, INF
        
        for x in nums:
            mod = x % 3
            if mod == 1:
                if x < m1_1:
                    m1_2 = m1_1
                    m1_1 = x
                elif x < m1_2:
                    m1_2 = x
            elif mod == 2:
                if x < m2_1:
                    m2_2 = m2_1
                    m2_1 = x
                elif x < m2_2:
                    m2_2 = x
        
        remove = INF
        
        if r == 1:
            # Option 1: remove one remainder-1 number
            remove = min(remove, m1_1)
            # Option 2: remove two remainder-2 numbers
            if m2_2 < INF:
                remove = min(remove, m2_1 + m2_2)
        else:
            # Option 1: remove one remainder-2 number
            remove = min(remove, m2_1)
            # Option 2: remove two remainder-1 numbers
            if m1_2 < INF:
                remove = min(remove, m1_1 + m1_2)
        
        return 0 if remove == INF else total - remove
