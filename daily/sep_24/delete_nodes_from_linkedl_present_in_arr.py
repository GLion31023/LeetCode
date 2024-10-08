from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def modified_list(nums: list[int], head: Optional[ListNode]) -> Optional[ListNode]:
    if not head:
        return

    nums = set(nums)

    while head and head.val in nums:
        head = head.next

    curr = head
    while curr.next:
        if curr.next.val in nums:
            curr.next = curr.next.next
        else:
            curr = curr.next

    return head
