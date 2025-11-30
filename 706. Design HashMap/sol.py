class MyHashMap:

    def __init__(self):
        self.bucket = 769
        self.hashmap = [[] for _ in range(self.bucket)]

    def put(self, key: int, value: int) -> None:
        flag = False
        for element in self.hashmap[key % self.bucket]:
            if element[0] == key:
                element[1] = value
                flag = True
                break
        
        if not flag:
            self.hashmap[key % self.bucket].append([key, value])


    def get(self, key: int) -> int:
        for element in self.hashmap[key % self.bucket]:
            if element[0] == key:
                return element[1]
        return -1

    def remove(self, key: int) -> None:
        bucket = self.hashmap[key % self.bucket]
        for i, element in enumerate(bucket):
            if element[0] == key:
                del bucket[i]
                break


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)