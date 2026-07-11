class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        def digit_sum(n):
            s = 0
            while n:
                s += n % 10
                n //= 10
            return s

        boxes = defaultdict(int)
        for i in range(lowLimit, highLimit + 1):
            boxes[digit_sum(i)] += 1

        return max(boxes.values())
