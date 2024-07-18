def decode_string(s: str) -> str:
    stack = []
    num = 0
    current_s = ''

    for c in s:
        if c.isdigit():
            num = num * 10 + int(c)
        elif c == '[':
            stack.append((current_s, num))
            current_s = ''
            num = 0
        elif c == ']':
            last_string, rep_count = stack.pop()
            current_s = last_string + current_s * rep_count
        else:
            current_s += c

    return current_s


print(decode_string("3[a]2[bc]"))
print(decode_string("3[a2[c]]"))
print(decode_string("2[abc]3[cd]ef"))
print(decode_string("100[leetcode]"))
