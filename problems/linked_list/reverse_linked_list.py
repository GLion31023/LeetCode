from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def list_to_linked_list(lst: list[int]) -> Optional[ListNode]:
    if not lst:
        return None
    head = ListNode(lst[0])
    curr = head
    for value in lst[1:]:
        curr.next = ListNode(value)
        curr = curr.next
    return head


def linked_list_to_list(head: Optional[ListNode]) -> list[int]:
    lst = []
    current = head
    while current:
        lst.append(current.val)
        current = current.next
    return lst


def reverse_list(head: Optional[ListNode]) -> Optional[ListNode]:
    prev = None

    while head:
        next_n = head.next  # 2
        head.next = prev    # 1 -> 2 => 1 -> None
        prev = head         # 1
        head = next_n       # 1 = 2

    head = prev

    return head


reversed_list = reverse_list(list_to_linked_list([1, 2, 3, 4, 5]))
print(linked_list_to_list(reversed_list))
