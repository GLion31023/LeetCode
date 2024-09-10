from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f"Val: {self.val}, next: {self.next} "


def lst_to_ll(lst: list[int]) -> Optional[ListNode]:
    if not lst:
        return

    head = ListNode(lst[0])
    curr = head

    for v in lst[1:]:
        curr.next = ListNode(v)
        curr = curr.next

    return head


def insert_gcd(head: Optional[ListNode]) -> Optional[ListNode]:
    if not head or not head.next:
        return head

    curr = head
    while curr.next:
        next_n = curr.next

        a, b = curr.val, next_n.val
        while b != 0:
            a, b = b, a % b

        curr.next = ListNode(a)
        curr = curr.next
        curr.next = next_n
        curr = curr.next

    return head


l1 = lst_to_ll([18, 6, 10, 3])
print(insert_gcd(l1))

# Example 1:
#
# Input: head = [18,6,10,3]
# Output: [18,6,6,2,10,1,3]
# Explanation: The 1st diagram denotes the initial linked list and the 2nd diagram denotes the linked list after
# inserting the new nodes (nodes in blue are the inserted nodes).
# - We insert the greatest common divisor of 18 and 6 = 6 between the 1st and the 2nd nodes.
# - We insert the greatest common divisor of 6 and 10 = 2 between the 2nd and the 3rd nodes.
# - We insert the greatest common divisor of 10 and 3 = 1 between the 3rd and the 4th nodes.
# There are no more adjacent nodes, so we return the linked list.

# Example 2:
#
# Input: head = [7]
# Output: [7]
# Explanation: The 1st diagram denotes the initial linked list and the 2nd diagram denotes the linked list after
# inserting the new nodes.
# There are no pairs of adjacent nodes, so we return the initial linked list.
#
#
# Constraints:
#
# The number of nodes in the list is in the range [1, 5000].
# 1 <= Node.val <= 1000
