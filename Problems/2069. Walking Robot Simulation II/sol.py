class Robot:
    def __init__(self, width: int, height: int):
        self.w = width
        self.h = height
        self.pos = 0
        self.moved = False

    def step(self, num: int) -> None:
        self.moved = True
        p = 2 * (self.w - 1) + 2 * (self.h - 1)
        self.pos = (self.pos + num) % p

    def getPos(self) -> list[int]:
        p = 2 * (self.w - 1) + 2 * (self.h - 1)
        curr = self.pos
        w, h = self.w, self.h

        if 0 <= curr < w:
            return [curr, 0]
        if w <= curr < w + h - 1:
            return [w - 1, curr - (w - 1)]
        if w + h - 1 <= curr < 2 * w + h - 2:
            return [w - 1 - (curr - (w + h - 2)), h - 1]

        return [0, h - 1 - (curr - (2 * w + h - 3))]

    def getDir(self) -> str:
        if not self.moved and self.pos == 0:
            return "East"
        
        p = 2 * (self.w - 1) + 2 * (self.h - 1)
        curr = self.pos
        w, h = self.w, self.h

        if curr == 0: return "South"
        
        if 1 <= curr < w: return "East"
        if w <= curr < w + h - 1: return "North"
        if w + h - 1 <= curr < 2 * w + h - 2: return "West"
        return "South"


# Your Robot object will be instantiated and called as such:
# obj = Robot(width, height)
# obj.step(num)
# param_2 = obj.getPos()
# param_3 = obj.getDir()