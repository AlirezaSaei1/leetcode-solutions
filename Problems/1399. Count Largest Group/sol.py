class Solution:
    def countLargestGroup(self, n: int) -> int:
        def sum_digits(n):
            summ = 0
            while n != 0:
                summ += (n % 10)
                n //= 10
            return summ 
        sums = [sum_digits(i) for i in range(1, n+1)]
        res = 0
        ctr = Counter(sums).values()
        maxx = max(ctr)
        for v in ctr:
            if v == maxx:
                res += 1
        
        return res
