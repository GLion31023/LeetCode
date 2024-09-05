def sum_digits_of_str(s: str, k: int) -> int:
    s_ds = "".join(map(lambda x: str(ord(x) - 96), s))
    res = 0

    for i in range(k):
        res = sum(int(c) for c in s_ds)
        s_ds = str(res)

    return res


print(sum_digits_of_str(s = "iiii", k = 1))
print(sum_digits_of_str(s = "leetcode", k = 2))
print(sum_digits_of_str(s = "zbax", k = 2))


# Example 1:
#
# Input: s = "iiii", k = 1
# Output: 36
# Explanation: The operations are as follows:
# - Convert: "iiii" ➝ "(9)(9)(9)(9)" ➝ "9999" ➝ 9999
# - Transform #1: 9999 ➝ 9 + 9 + 9 + 9 ➝ 36
# Thus the resulting integer is 36.

# Example 2:
#
# Input: s = "leetcode", k = 2
# Output: 6
# Explanation: The operations are as follows:
# - Convert: "leetcode" ➝ "(12)(5)(5)(20)(3)(15)(4)(5)" ➝ "12552031545" ➝ 12552031545
# - Transform #1: 12552031545 ➝ 1 + 2 + 5 + 5 + 2 + 0 + 3 + 1 + 5 + 4 + 5 ➝ 33
# - Transform #2: 33 ➝ 3 + 3 ➝ 6
# Thus the resulting integer is 6.

# Example 3:
#
# Input: s = "zbax", k = 2
# Output: 8
