class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def lst_to_linked_list(lst: list[int]) -> ListNode:
    head = ListNode(lst[0])
    curr = head

    for v in lst[1:]:
        curr.next = ListNode(v)
        curr = curr.next

    return head


def get_dec_val(head: ListNode) -> int:
    res = 0

    while head:
        res = 2 * res + head.val
        head = head.next

    return res

    # bin_val = ""
    #
    # while head:
    #     bin_val += str(head.val)
    #     head = head.next
    #
    # return int(bin_val, 2)


ll = lst_to_linked_list([1, 0, 1])
ll1 = lst_to_linked_list([0])

print(get_dec_val(ll))
print(get_dec_val(ll1))


# Example 1:
#
# Input: head = [1,0,1]
# Output: 5
# Explanation: (101) in base 2 = (5) in base 10

# Example 2:
#
# Input: head = [0]
# Output: 0
