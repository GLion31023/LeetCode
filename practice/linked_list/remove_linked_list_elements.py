from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f"node_value({self.val})"


def lst_to_ll(lst: list[int]) -> Optional[ListNode]:
    if not lst:
        return

    head = ListNode(lst[0])

    curr = head
    for v in lst[1:]:
        curr.next = ListNode(v)
        curr = curr.next

    return head


def remove_elements(head: Optional[ListNode], val: int) -> Optional[ListNode]:
    dummy = ListNode(0)
    dummy.next = head
    current = dummy

    while current.next:
        if current.next.val == val:
            current.next = current.next.next
        else:
            current = current.next

    return dummy.next


ll1 = lst_to_ll([1, 2, 6, 3, 4, 5, 6])
ll2 = lst_to_ll([1, 2, 6, 3, 4, 5, 6])
ll3 = lst_to_ll([1, 2, 6, 3, 4, 5, 6])

print(remove_elements(ll1, 6))
print(remove_elements(ll2, 1))
print(remove_elements(ll3, 7))

# Example 1:
#
# Input: head = [1,2,6,3,4,5,6], val = 6
# Output: [1,2,3,4,5]

# Example 2:
#
# Input: head = [], val = 1
# Output: []

# Example 3:
#
# Input: head = [7,7,7,7], val = 7
# Output: []
#
# Constraints:
#
# The number of nodes in the list is in the range [0, 10^4].
# 1 <= Node.val <= 50
# 0 <= val <= 50
