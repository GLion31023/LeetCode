def rotate_string(s: str, goal: str) -> bool:
    for _ in range(len(s)):
        if s == goal:
            return True
        s = s[1:] + s[0]

    return False


print(rotate_string(s="abcde", goal="cdeab"))
print(rotate_string(s="abcde", goal="abced"))

# Example 1:
# Input: s = "abcde", goal = "cdeab"
# Output: true

# Example 2
# Input: s = "abcde", goal = "abced"
# Output: false
