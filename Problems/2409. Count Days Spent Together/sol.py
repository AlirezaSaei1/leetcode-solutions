class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        def dayOfYear(date_str: str) -> int:
            m, d = map(int, date_str.split('-'))
            return sum(months[:m-1]) + d

        arriveA = dayOfYear(arriveAlice)
        leaveA = dayOfYear(leaveAlice)
        arriveB = dayOfYear(arriveBob)
        leaveB = dayOfYear(leaveBob)

        overlap_start = max(arriveA, arriveB)
        overlap_end = min(leaveA, leaveB)

        return max(0, overlap_end - overlap_start + 1)