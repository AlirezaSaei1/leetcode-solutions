class Solution:
    def convertTime(self, current: str, correct: str) -> int:
        current = list(map(int, current.split(':')))
        correct = list(map(int, correct.split(':')))

        cur_minute = current[0] * 60 + current[1]
        cor_minute = correct[0] * 60 + correct[1]
        diff = abs(cor_minute - cur_minute)

        count = 0

        count += diff // 60
        diff %= 60

        count += diff // 15
        diff %= 15

        count += diff // 5
        diff %= 5

        return count + diff

