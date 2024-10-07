def min_len(s: str) -> int:
    stack = []

    for c in s:
        if stack and c == 'B':
            if stack[-1] == 'A':
                stack.pop()
                continue

        if stack and c == 'D':
            if stack[-1] == 'C':
                stack.pop()
                continue

        stack.append(c)

    return len(stack)


print(min_len("ABFCACDB"))
print(min_len("ACBBD"))


# Example 1:
# Input: s = "ABFCACDB"
# Output: 2
# Explanation: We can do the following operations:
# - Remove the substring "ABFCACDB", so s = "FCACDB".
# - Remove the substring "FCACDB", so s = "FCAB".
# - Remove the substring "FCAB", so s = "FC".
# So the resulting length of the string is 2.
# It can be shown that it is the minimum length that we can obtain.

# Example 2:
# Input: s = "ACBBD"
# Output: 5
# Explanation: We cannot do any operations on the string so the length remains the same.
