from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f"node_value({self.val})"


def list_to_ll(lst: list[int]) -> Optional[ListNode]:
    if not lst:
        return None

    head = ListNode(lst[0])
    curr = head

    for v in lst[1:]:
        curr.next = ListNode(v)
        curr = curr.next

    return head


def is_palindrome(head: Optional[ListNode]) -> bool:
    if not head.next:
        return True

    slow = fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    mid = slow
    prev = None

    while mid:
        next_n = mid.next
        mid.next = prev
        prev = mid
        mid = next_n

    mid = prev

    while mid:
        if not mid.val == head.val:
            return False
        mid = mid.next
        head = head.next

    return True


l1 = list_to_ll([1, 2, 2, 1])
l2 = list_to_ll([1, 2])

print(is_palindrome(l1))
print(is_palindrome(l2))

# Example 1:
#
# Input: head = [1,2,2,1]
# Output: true

# Example 2:
#
# Input: head = [1,2]
# Output: false
#
# Constraints:
# The number of nodes in the list is in the range [1, 10^5].
# 0 <= Node.val <= 9
#
# Follow up: Could you do it in O(n) time and O(1) space?
