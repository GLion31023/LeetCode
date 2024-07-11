def reverse_parentheses(s: str) -> str:
    stack = []

    for char in s:
        if char == ")":
            temp = []
            while stack and stack[-1] != '(':
                temp.append(stack.pop())
            stack.pop()
            stack.extend(temp)
        else:
            stack.append(char)

    return "".join(stack)


print(reverse_parentheses("(abcd)"))
print(reverse_parentheses("(u(love)i)"))
print(reverse_parentheses("(ed(et(oc))el)"))
