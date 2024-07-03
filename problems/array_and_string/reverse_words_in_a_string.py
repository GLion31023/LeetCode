def reverse_words(s: str) -> str:
    # without built-in functions
    rev_words = []
    new_word = False
    end = len(s)

    for i in range(len(s) - 1, -1, -1):
        if s[i] == " ":
            if new_word:
                rev_words.append(s[i + 1:end])
                new_word = False
            end = i
        else:
            if not new_word:
                new_word = True
                end = i + 1

    if new_word:
        rev_words.append(s[:end])

    return " ".join(rev_words)

    # with built-in:
    # return " ".join(s.split()[::-1])


print(reverse_words(s="the sky is blue"))
print(reverse_words(s="  hello world  "))
print(reverse_words(s="a good   example"))
