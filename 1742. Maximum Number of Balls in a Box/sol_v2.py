class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        boxes = defaultdict(int)

        def next_sum(s, n):
            n += 1
            while n % 10 == 0:
                s -= 9
                n //= 10
            return s + 1

        curr_sum = sum(map(int, str(lowLimit)))
        boxes[curr_sum] += 1

        for i in range(lowLimit, highLimit):
            curr_sum = next_sum(curr_sum, i)
            boxes[curr_sum] += 1

        return max(boxes.values())
