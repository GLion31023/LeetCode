from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def sort_list(head: Optional[ListNode]) -> Optional[ListNode]:
    if not head:
        return

    vals = []
    curr = head
    while curr:
        vals.append(curr.val)
        curr = curr.next

    vals.sort()
    curr = head
    for v in vals:
        curr.val = v
        curr = curr.next

    return head
