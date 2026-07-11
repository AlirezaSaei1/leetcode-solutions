class OrderedStream:

    def __init__(self, n: int):
        self.stream = [None] * (n + 1)
        self.pointer = 1
        self.n = n

    def insert(self, idKey: int, value: str) -> List[str]:
        self.stream[idKey] = value
        
        output = []
        while self.pointer < self.n + 1 and self.stream[self.pointer] is not None:
            output.append(self.stream[self.pointer])
            self.pointer += 1
        
        return output


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)