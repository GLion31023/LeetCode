from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def delete_middle(head: Optional[ListNode]) -> Optional[ListNode]:
    if not head or not head.next:
        return None

    fast = slow = head
    pre_slow = None

    while fast and fast.next:
        pre_slow = slow
        slow = slow.next
        fast = fast.next.next

    if pre_slow:
        pre_slow.next = slow.next
        slow.next = None

    return head