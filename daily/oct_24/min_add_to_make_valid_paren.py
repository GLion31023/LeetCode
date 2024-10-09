def make_valid(s: str) -> int:
    adds = 0
    left = 0

    for c in s:
        if c == '(':
            left += 1
        else:
            if left:
                left -= 1
            else:
                adds += 1

    return adds + left


print(make_valid("())"))
print(make_valid("((("))
print(make_valid("()))(("))

# Example 1:
# Input: s = "())"
# Output: 1

# Example 2:
# Input: s = "((("
# Output: 3
