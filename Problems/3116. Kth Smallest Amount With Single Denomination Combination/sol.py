class Solution:
    def findKthSmallest(self, coins: list[int], k: int) -> int:
        coins = sorted(list(set(coins)))
        filtered = []
        for c in coins:
            if not any(c % f == 0 for f in filtered):
                filtered.append(c)
                
        n = len(filtered)
        plus = []
        minus = []
        
        max_val = k * filtered[0]
        
        for i in range(1, 1 << n):
            curr_lcm = 1
            bits = 0
            for j in range(n):
                if i & (1 << j):
                    curr_lcm = math.lcm(curr_lcm, filtered[j])
                    bits += 1
                    if curr_lcm > max_val:
                        break
                        
            if curr_lcm <= max_val:
                if bits % 2 == 1:
                    plus.append(curr_lcm)
                else:
                    minus.append(curr_lcm)
                    
        left = 1
        right = max_val
        
        while left < right:
            mid = (left + right) // 2
            cnt = sum(mid // l for l in plus) - sum(mid // l for l in minus)
            
            if cnt >= k:
                right = mid
            else:
                left = mid + 1
                
        return left