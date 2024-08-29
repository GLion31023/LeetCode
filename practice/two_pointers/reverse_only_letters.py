def reverse_letters(s: str) -> str:
    res = list(s)
    l, r = 0, len(s) - 1

    def is_letter(char):
        return (ord("A") <= ord(char) <= ord("Z") or
                ord("a") <= ord(char) <= ord("z"))

    while l < r:
        if is_letter(res[l]) and is_letter(res[r]):
            res[l], res[r] = res[r], res[l]
            l += 1
            r -= 1
        elif is_letter(s[l]):
            r -= 1
        else:
            l += 1

    return "".join(res)


print(reverse_letters(s="ab-cd"))
print(reverse_letters(s="a-bC-dEf-ghIj"))
print(reverse_letters(s="Test1ng-Leet=code-Q!"))
