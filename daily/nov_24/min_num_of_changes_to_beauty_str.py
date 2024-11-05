def min_changes(s: str) -> int:
    changes = 0

    for i in range(1, len(s), 2):
        if s[i] != s[i - 1]:
            changes += 1

    return changes


print(min_changes("1001"))
print(min_changes("10"))
print(min_changes("0000"))

# Example 1:
# Input: s = "1001"
# Output: 2
# Explanation: We change s[1] to 1 and s[3] to 0 to get string "1100".
# It can be seen that the string "1100" is beautiful because we can partition it into "11|00".
# It can be proven that 2 is the minimum number of changes needed to make the string beautiful.

# Example 2:
# Input: s = "10"
# Output: 1
# Explanation: We change s[1] to 1 to get string "11".
# It can be seen that the string "11" is beautiful because we can partition it into "11".
# It can be proven that 1 is the minimum number of changes needed to make the string beautiful.

# Example 3:
# Input: s = "0000"
# Output: 0
# Explanation: We don't need to make any changes as the string "0000" is beautiful already.
