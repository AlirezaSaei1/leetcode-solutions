class Solution:
    def bestClosingTime(self, customers: str) -> int:
        n = len(customers)
        ys = customers.count('Y')

        earliest = 0
        min_penalty = float('inf')
        cur_y, cur_n = 0, 0

        min_penalty = ys
        earliest = 0

        for i in range(n):
            cur_sc = cur_n + (ys - cur_y)

            if min_penalty > cur_sc:
                earliest = i
                min_penalty = cur_sc

            if customers[i] == 'Y':
                cur_y += 1
            else:
                cur_n += 1
        
        cur_sc = cur_n
        if cur_sc < min_penalty:
            earliest = n

        return earliest
