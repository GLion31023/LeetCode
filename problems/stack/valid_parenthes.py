def is_valid(s: str) -> bool:
    stack = []

    for p in s:
        if p in '([{':
            stack.append(p)
        else:
            if not stack:
                return False
            i = stack.pop()
            if i == '(' and p != ')':
                return False
            elif i == '[' and p != ']':
                return False
            elif i == '{' and p != '}':
                return False

    return len(stack) == 0


print(is_valid("()"))
print(is_valid("()[]{}"))
print(is_valid("(]"))
print(is_valid("([])"))

# Example 1:
# Input: s = "()"
#
# Output: true
#
# Example 2:
# Input: s = "()[]{}"
#
# Output: true
#
# Example 3:
# Input: s = "(]"
#
# Output: false
#
# Example 4:
# Input: s = "([])"
#
# Output: true
