class Solution:
    def numberOfWays(self, corridor: str) -> int:
        seat_count = corridor.count('S')
        if seat_count == 0 or seat_count % 2 != 0:
            return 0

        MOD = 10 ** 9 + 7
        sc, i, k = 0, 0, 0
        answer = 1
        n = len(corridor)

        while i < n:
            if corridor[i] == 'S':
                sc += 1
            else:
                if sc != 0 and sc % 2 == 0 and sc < seat_count:
                    while i < n and corridor[i] == 'P':
                        k += 1
                        i += 1

                    answer = (answer * (k+1)) % MOD
                    k = 0
                    continue
            i+=1
        
        return answer