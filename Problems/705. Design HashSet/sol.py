class MyHashSet:

    def __init__(self):
        self.bucket = 769
        self.hashset = [[] for _ in range(self.bucket)]

    def add(self, key: int) -> None:
        if not self.contains(key):
            self.hashset[key % self.bucket].append(key)

    def remove(self, key: int) -> None:
        if self.contains(key):
            self.hashset[key % self.bucket].remove(key)

    def contains(self, key: int) -> bool:
        return key in self.hashset[key % self.bucket]


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)