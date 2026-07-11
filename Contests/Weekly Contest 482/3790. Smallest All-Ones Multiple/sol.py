class Solution:
    def minAllOneMultiple(self, k: int) -> int:
        if k % 2 == 0 or k % 5 == 0:
            return -1

        r = 0
        remainders = set()
        for i in range(1, k+1):
            next = r * 10 + 1
            r = next % k

            if r == 0:
                return i

            if r in remainders:
                return -1

            remainders.add(r)

        return -1
            