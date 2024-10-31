import heapq


class SmallestInfiniteSet:
    def __init__(self):
        self.nums = [x for x in range(1, 1001)]
        self.not_active = set()
        heapq.heapify(self.nums)

    def pop_smallest(self) -> int:
        num = heapq.heappop(self.nums)
        self.not_active.add(num)
        return num

    def add_back(self, num: int) -> None:
        if num in self.not_active:
            self.not_active.remove(num)
            heapq.heappush(self.nums, num)


ss = SmallestInfiniteSet()
print(ss.add_back(2))
print(ss.pop_smallest())
print(ss.pop_smallest())
print(ss.pop_smallest())
print(ss.add_back(1))
print(ss.pop_smallest())
print(ss.pop_smallest())
print(ss.pop_smallest())

# Example 1:
#
# Input ["SmallestInfiniteSet", "addBack", "popSmallest", "popSmallest", "popSmallest", "addBack", "popSmallest",
# "popSmallest", "popSmallest"] [[], [2], [], [], [], [1], [], [], []]
# Output [null, null, 1, 2, 3, null, 1, 4, 5]
#
# Explanation
# SmallestInfiniteSet smallestInfiniteSet = new SmallestInfiniteSet();
# smallestInfiniteSet.addBack(2);    // 2 is already in the set, so no change is made.
# smallestInfiniteSet.popSmallest(); // return 1, since 1 is the smallest number, and remove it from the set.
# smallestInfiniteSet.popSmallest(); // return 2, and remove it from the set.
# smallestInfiniteSet.popSmallest(); // return 3, and remove it from the set.
# smallestInfiniteSet.addBack(1);    // 1 is added back to the set.
# smallestInfiniteSet.popSmallest(); // return 1, since 1 was added back to the set and
#                                    // is the smallest number, and remove it from the set.
# smallestInfiniteSet.popSmallest(); // return 4, and remove it from the set.
# smallestInfiniteSet.popSmallest(); // return 5, and remove it from the set.
