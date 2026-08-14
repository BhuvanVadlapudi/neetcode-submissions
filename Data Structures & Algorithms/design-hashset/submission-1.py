class MyHashSet:

    def __init__(self):
        self.data = [False for _ in range(10**6+1)]

    def add(self, key: int) -> None:
        if(self.contains(key)):
            return
        self.data[key] = True

    def remove(self, key: int) -> None:
        self.data[key] = False

    def contains(self, key: int) -> bool:
        if(self.data[key]):
            return True
        return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)