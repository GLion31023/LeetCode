from collections import defaultdict


def equal_occurrences(s: str) -> bool:
    count = defaultdict(int)

    for c in s:
        count[c] += 1

    values = list(count.values())

    for i in range(1, len(values)):
        if values[i] != values[i - 1]:
            return False

    return True


print(equal_occurrences("abacbc"))
print(equal_occurrences("aaabb"))

# Example 1:
# Input: s = "abacbc"
# Output: true
# Explanation: The characters that appear in s are 'a', 'b', and 'c'. All characters occur 2 times in s.

# Example 2:
# Input: s = "aaabb"
# Output: false
# Explanation: The characters that appear in s are 'a' and 'b'.
# 'a' occurs 3 times while 'b' occurs 2 times, which is not the same number of times.
