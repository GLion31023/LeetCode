from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f"I'm: {self.val}, my next: {self.next}"


def list_to_ll(lst: list[int]) -> Optional[ListNode]:
    if not lst:
        return

    head = ListNode(lst[0])
    curr = head

    for v in lst[1:]:
        curr.next = ListNode(v)
        curr = curr.next

    return head


def add_two_numbers(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    dummy = ListNode()
    curr = dummy
    rem = 0

    while l1 or l2 or rem:
        a = l1.val if l1 else 0
        b = l2.val if l2 else 0

        total = a + b + rem
        rem = total // 10
        curr.next = ListNode(total % 10)
        curr = curr.next

        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None

    return dummy.next

    # nums = [[] for _ in range(2)]
    #
    # while l1 or l2:
    #     if l1:
    #         nums[0].append(str(l1.val))
    #         l1 = l1.next
    #     if l2:
    #         nums[1].append(str(l2.val))
    #         l2 = l2.next
    #
    # res = int("".join(nums[0][::-1])) + int("".join(nums[1][::-1]))
    #
    # dummy = ListNode()
    # curr = dummy
    #
    # for n in (str(res)[::-1]):
    #     curr.next = ListNode(int(n))
    #     curr = curr.next

    # return dummy.next


ll1 = list_to_ll([2, 4, 3])
ll2 = list_to_ll([5, 6, 4])
ll3 = list_to_ll([0])
ll4 = list_to_ll([0])
ll5 = list_to_ll([9, 9, 9, 9, 9, 9, 9])
ll6 = list_to_ll([9, 9, 9, 9])
ll7 = list_to_ll([2, 4, 9])
ll8 = list_to_ll([5, 6, 4, 9])

print(add_two_numbers(ll1, ll2))
print(add_two_numbers(ll3, ll4))
print(add_two_numbers(ll5, ll6))
print(add_two_numbers(ll7, ll8))

# Example 1:
#
# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]
# Explanation: 342 + 465 = 807.

# Example 2:
#
# Input: l1 = [0], l2 = [0]
# Output: [0]

# Example 3:
#
# Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
# Output: [8,9,9,9,0,0,0,1]
