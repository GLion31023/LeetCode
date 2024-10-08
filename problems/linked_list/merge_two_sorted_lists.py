from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f"I'm: {self.val}, my next: {self.next}"


def lst_to_ll(lst: list[int]) -> Optional[ListNode]:
    if not lst:
        return

    head = ListNode(lst[0])
    curr = head

    for v in lst[1:]:
        curr.next = ListNode(v)
        curr = curr.next

    return head


def merge_sorted_lists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    if not list1:
        return list2

    if not list2:
        return list1

    dummy = ListNode()
    curr = dummy

    while list1 and list2:
        if list1.val <= list2.val:
            curr.next = list1
            list1 = list1.next
        else:
            curr.next = list2
            list2 = list2.next
        curr = curr.next

    if list1:
        curr.next = list1
    else:
        curr.next = list2

    return dummy.next


ll1 = lst_to_ll([1,2,4])
ll2 = lst_to_ll([1,3,4])
ll3 = lst_to_ll([])
ll4 = lst_to_ll([])
ll5 = lst_to_ll([])
ll6 = lst_to_ll([0])
print(merge_sorted_lists(ll1, ll2))
print(merge_sorted_lists(ll3, ll4))
print(merge_sorted_lists(ll5, ll6))


# Example 1:
#
# Input: list1 = [1,2,4], list2 = [1,3,4]
# Output: [1,1,2,3,4,4]

# Example 2:
#
# Input: list1 = [], list2 = []
# Output: []

# Example 3:
#
# Input: list1 = [], list2 = [0]
# Output: [0]
