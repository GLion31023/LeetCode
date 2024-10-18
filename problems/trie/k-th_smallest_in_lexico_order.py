def find_kth_number(n: int, k: int) -> int:
    def get_steps(curr, next_n, n):
        steps = 0
        while curr <= n:
            steps += min(n + 1, next_n) - curr
            curr *= 10
            next_n *= 10
        return steps

    curr = 1
    k -= 1
    while k > 0:
        steps = get_steps(curr, curr + 1, n)
        if steps <= k:
            curr += 1
            k -= steps
        else:
            curr *= 10
            k -= 1
    return curr


# Example 1:
#
# Input: n = 13, k = 2
# Output: 10
# Explanation: The lexicographical order is [1, 10, 11, 12, 13, 2, 3, 4, 5, 6, 7, 8, 9],
# so the second-smallest number is 10.
# Example 2:
#
# Input: n = 1, k = 1
# Output: 1
