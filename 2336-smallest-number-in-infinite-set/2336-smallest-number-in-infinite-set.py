from sortedcontainers import SortedSet
class SmallestInfiniteSet:

    def __init__(self):
        self.s1 = SortedSet()
        for i in range(1,1002):
            self.s1.add(i)        

    def popSmallest(self) -> int:
        x = self.s1[0]
        self.s1.remove(x)
        return x        

    def addBack(self, num: int) -> None:
        self.s1.add(num)
        


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)