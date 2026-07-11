class Solution:
    def readBinaryWatch(self, turnedOn: int) -> list[str]:
        result = []

        for hour in range(12):        # 0–11
            for minute in range(60):  # 0–59
                if bin(hour).count('1') + bin(minute).count('1') == turnedOn:
                    time_str = f"{hour}:{minute:02d}"
                    result.append(time_str)

        return result
