def reverse_prefix(word: str, ch: str) -> str:
    stack = []
    rev_word = ''

    for i, c in enumerate(word):
        if not c == ch:
            stack.append(c)
            if i == len(word) - 1:
                return word
        else:
            rev_word += c
            while stack:
                rc = stack.pop()
                rev_word += rc
            rev_word += word[i + 1:]
            break

    return rev_word


print(reverse_prefix(word="abcdefd", ch="d"))
print(reverse_prefix(word="xyxzxe", ch="z"))
print(reverse_prefix(word="abcd", ch="z"))
