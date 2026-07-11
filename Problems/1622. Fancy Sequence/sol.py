class Fancy:
    def __init__(self):
        self.seq = []
        self.a = 1
        self.b = 0
        self.MOD = 10**9 + 7

    def append(self, val: int) -> None:
        inv_a = pow(self.a, self.MOD - 2, self.MOD)
        self.seq.append(((val - self.b) * inv_a) % self.MOD)

    def addAll(self, inc: int) -> None:
        self.b = (self.b + inc) % self.MOD

    def multAll(self, m: int) -> None:
        self.a = (self.a * m) % self.MOD
        self.b = (self.b * m) % self.MOD

    def getIndex(self, idx: int) -> int:
        if idx >= len(self.seq):
            return -1
        return (self.seq[idx] * self.a + self.b) % self.MOD

# Your Fancy object will be instantiated and called as such:
# obj = Fancy()
# obj.append(val)
# obj.addAll(inc)
# obj.multAll(m)
# param_4 = obj.getIndex(idx)