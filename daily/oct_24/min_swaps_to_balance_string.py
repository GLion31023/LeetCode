def min_swaps(s: str) -> int:
    swaps = 0
    balance = 0

    for c in s:
        if c == '[':
            balance -= 1
        elif c == ']':
            balance += 1

        if balance > 0:
            swaps += 1
            balance -= 2

    return swaps


print(min_swaps("][]["))
print(min_swaps("]]][[["))
print(min_swaps("[]"))
print(min_swaps("][][]["))


# Example 1:
# Input: s = "][]["
# Output: 1
# Explanation: You can make the string balanced by swapping index 0 with index 3.
# The resulting string is "[[]]".

# Example 2:
# Input: s = "]]][[["
# Output: 2
# Explanation: You can do the following to make the string balanced:
# - Swap index 0 with index 4. s = "[]][][".
# - Swap index 1 with index 5. s = "[[][]]".
# The resulting string is "[[][]]".

# Example 3:
# Input: s = "[]"
# Output: 0
# Explanation: The string is already balanced.
