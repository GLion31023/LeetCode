# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def pair_sum(head: Optional[ListNode]) -> int:
    fast = slow = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    prev = None
    while slow:
        next_node = slow.next
        slow.next = prev
        prev = slow
        slow = next_node

    max_sum = 0
    while prev:
        max_sum = max(max_sum, (head.val + prev.val))
        head = head.next
        prev = prev.next

    return max_sum
