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

    for v in lst[1:]:
        curr.next = ListNode(v)
        curr = curr.next

    return head


def spiral_matrix(m: int, n: int, head: Optional[ListNode]) -> list[list[int]]:
    matrix = [[-1] * n for _ in range(m)]
    dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    cur_d = 0
    x, y = 0, 0

    curr = head
    for _ in range(m * n):
        if curr:
            matrix[x][y] = curr.val
            curr = curr.next
        else:
            break

        next_x = x + dirs[cur_d][0]
        next_y = y + dirs[cur_d][1]

        if not (0 <= next_x < m and 0 <= next_y < n and matrix[next_x][next_y] == -1):
            cur_d = (cur_d + 1) % 4
            next_x = x + dirs[cur_d][0]
            next_y = y + dirs[cur_d][1]

        x, y = next_x, next_y

    return matrix


ll = list_to_linked_list([3, 0, 2, 6, 8, 1, 7, 9, 4, 2, 5, 5, 0])
ll1 = list_to_linked_list([0, 1, 2])

print(spiral_matrix(3, 5, ll))
print(spiral_matrix(1, 4, ll1))

# Example 1:
#
# Input: m = 3, n = 5, head = [3,0,2,6,8,1,7,9,4,2,5,5,0]
# Output: [[3,0,2,6,8],[5,0,-1,-1,1],[5,2,4,9,7]]
# Explanation: The diagram above shows how the values are printed in the matrix.
# Note that the remaining spaces in the matrix are filled with -1.

# Example 2:
#
# Input: m = 1, n = 4, head = [0,1,2]
# Output: [[0,1,2,-1]]
# Explanation: The diagram above shows how the values are printed from left to right in the matrix.
# The last space in the matrix is set to -1.
