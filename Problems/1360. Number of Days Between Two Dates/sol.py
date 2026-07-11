class Solution:
    def daysBetweenDates(self, date1: str, date2: str) -> int:
        def isLeap(year):
            return (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0)

        days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        def daysFrom1900(date):
            year, month, day = map(int, date.split('-'))
            days = 0

            for y in range(1900, year):
                days += 366 if isLeap(y) else 365

            for m in range(1, month):
                days += days_in_month[m-1]
                if m == 2 and isLeap(year):
                    days += 1
            days += day

            return days

        return abs(daysFrom1900(date1) - daysFrom1900(date2))