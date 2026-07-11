class Solution:
    def average(self, salary: List[int]) -> float:
        minn = float('inf')
        maxx = float('-inf')
        summ = 0
        count = 0

        for s in salary:
            if minn > s:
                minn = s
            
            if maxx < s:
                maxx = s

            summ += s
            count += 1
        
        summ -= maxx
        summ -= minn

        return summ / (count - 2)
