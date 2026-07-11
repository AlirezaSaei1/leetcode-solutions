class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        counter = 0
        value = 1

        for num in arr:
            while value < num:
                counter += 1
                if counter == k:
                    return value

                value += 1
            value += 1

        while counter != k:
            value += 1
            counter += 1

        return value - 1
                