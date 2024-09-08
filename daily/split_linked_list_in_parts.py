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


def split_linked_list(head: Optional[ListNode], k: int) -> list[Optional[ListNode]]:
    len_ll = 0
    curr = head
    while curr:
        len_ll += 1
        curr = curr.next

    part_size = len_ll // k
    rem = len_ll % k

    result = []

    curr = head

    for i in range(k):
        part_head = curr
        part_len = part_size + (1 if rem > 0 else 0)
        rem -= 1

        for j in range(part_len - 1):
            if curr:
                curr = curr.next

        if curr:
            next_part = curr.next
            curr.next = None
            curr = next_part

        result.append(part_head)

    return result


l_list = list_to_linked_list([1, 2, 3])
l_list2 = list_to_linked_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

print(split_linked_list(l_list, k=5))
print(split_linked_list(l_list2, k=3))

# Example 1:
#
# Input: head = [1,2,3], k = 5
# Output: [[1],[2],[3],[],[]]
# Explanation:
# The first element output[0] has output[0].val = 1, output[0].next = null.
# The last element output[4] is null, but its string representation as a ListNode is [].

# Example 2:
#
# Input: head = [1,2,3,4,5,6,7,8,9,10], k = 3
# Output: [[1,2,3,4],[5,6,7],[8,9,10]]
# Explanation:
# The input has been split into consecutive parts with size difference at most 1, and earlier parts are a larger size
# than the later parts.
