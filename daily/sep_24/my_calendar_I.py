class MyCalendar:

    def __init__(self):
        self.events: list[list] = []

    def book(self, start: int, end: int) -> bool:
        s, e = 0, len(self.events) - 1
        insert_pos = 0

        while s <= e:
            mid = (s + e) // 2
            if self.events[mid][0] < start:
                s = mid + 1
            else:
                e = mid - 1

        insert_pos = s

        if insert_pos > 0 and self.events[insert_pos - 1][1] > start:
            return False

        if insert_pos < len(self.events) and self.events[insert_pos][0] < end:
            return False

        self.events.insert(insert_pos, [start, end])
        return True


obj = MyCalendar()
print(obj.book(10, 20))
print(obj.book(15, 25))
print(obj.book(20, 30))
print(obj.events)

# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)


# Example 1:
# Input
# ["MyCalendar", "book", "book", "book"]
# [[], [10, 20], [15, 25], [20, 30]]
# Output
# [null, true, false, true]
#
# Explanation
# MyCalendar myCalendar = new MyCalendar();
# myCalendar.book(10, 20); // return True
# myCalendar.book(15, 25); // return False, It can not be booked because time 15 is already booked by another event.
# myCalendar.book(20, 30); // return True, The event can be booked, as the first event takes every time less than 20,
# but not including 20.
