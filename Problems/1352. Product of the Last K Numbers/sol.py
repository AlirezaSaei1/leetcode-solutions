class ProductOfNumbers:

    def __init__(self):
        self.nums = []
        self.n = 0

    def add(self, num: int) -> None:
        if num != 0:
            if self.nums:
                self.nums.append(num * self.nums[-1])
            else:
                self.nums.append(num)
            self.n += 1
        else:
            self.nums.clear()
            self.n = 0

    def getProduct(self, k: int) -> int:
        if self.n < k:
            return 0
        elif self.n == k:
            return self.nums[-1]
        else:
            return self.nums[-1] // self.nums[-k - 1]



# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)