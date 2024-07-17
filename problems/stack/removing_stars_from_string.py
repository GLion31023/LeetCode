def remove_stars(s: str) -> str:
    stack = []

    for c in s:
        if c != "*":
            stack.append(c)
        else:
            stack.pop()

    return "".join(stack)


print(remove_stars("leet**cod*e"))
print(remove_stars("erase*****"))
