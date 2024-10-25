from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f"{self.val} -> {self.next}"


def swap_pairs(head: Optional[ListNode]) -> Optional[ListNode]:
    if not head or not head.next:
        return head

    dummy = ListNode(0)
    dummy.next = head
    prev = dummy
    curr = head

    while curr and curr.next:
        first = curr
        second = curr.next
        prev.next = second
        first.next = second.next
        second.next = first

        prev = first
        curr = first.next

    return dummy.next


def list_to_ll(lst: list[int]) -> Optional[ListNode]:
    if not lst:
        return

    head = ListNode(lst[0])
    curr = head

    for v in lst[1:]:
        curr.next = ListNode(v)
        curr = curr.next

    return head


ll1 = list_to_ll([1, 2, 3, 4])
print(swap_pairs(ll1))
