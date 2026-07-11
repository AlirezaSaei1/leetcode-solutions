class Solution:
    def dayOfYear(self, date: str) -> int:
        days = 0
        days_list = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        y, m, d = map(int, date.split('-'))

        days = sum(days_list[:m-1]) + d

        if (y % 400 == 0) or (y % 4 == 0 and y % 100 != 0):
            if m > 2:
                days += 1
        
        return days

        
