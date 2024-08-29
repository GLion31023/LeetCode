def reverse_letters(s: str) -> str:
    res = list(s)
    l, r = 0, len(s) - 1

    while l < r:
        if s[l].isalpha() and s[r].isalpha():
            res[l], res[r] = res[r], res[l]
            l += 1
            r -= 1
        elif s[l].isalpha():
            r -= 1
        else:
            l += 1

    return "".join(res)


print(reverse_letters(s="ab-cd"))
print(reverse_letters(s="a-bC-dEf-ghIj"))
print(reverse_letters(s="Test1ng-Leet=code-Q!"))
