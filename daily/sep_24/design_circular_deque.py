class MyCircularDeque:

    def __init__(self, k: int):
        self.deque: list = []
        self.max_l = k

    def insertFront(self, value: int) -> bool:
        if len(self.deque) == self.max_l:
            return False

        self.deque.insert(0, value)
        return True

    def insertLast(self, value: int) -> bool:
        if len(self.deque) == self.max_l:
            return False

        self.deque.append(value)
        return True

    def deleteFront(self) -> bool:
        if not self.deque:
            return False

        self.deque.pop(0)
        return True

    def deleteLast(self) -> bool:
        if not self.deque:
            return False

        self.deque.pop(-1)
        return True

    def getFront(self) -> int:
        if self.deque:
            return self.deque[0]

        return -1

    def getRear(self) -> int:
        if self.deque:
            return self.deque[-1]

        return -1

    def isEmpty(self) -> bool:
        if not self.deque:
            return True

        return False

    def isFull(self) -> bool:
        if len(self.deque) == self.max_l:
            return True

        return False


deque = MyCircularDeque(3)
print(deque.insertLast(1))
print(deque.insertLast(2))
print(deque.insertFront(3))
print(deque.insertFront(4))
print(deque.getRear())
print(deque.isFull())
print(deque.deleteLast())
print(deque.insertFront(4))
print(deque.getFront())

# Example 1:
#
# Input ["MyCircularDeque", "insertLast", "insertLast", "insertFront", "insertFront", "getRear", "isFull",
# "deleteLast", "insertFront", "getFront"] [[3], [1], [2], [3], [4], [], [], [], [4], []] Output [null, true, true,
# true, false, 2, true, true, true, 4]

# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()
