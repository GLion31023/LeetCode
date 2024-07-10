def is_subsequence(s: str, t: str) -> bool:
    read_s = 0
    i = 0

    if len(s) == 0:
        return True

    while i <= len(t) - 1:
        if s[read_s] == t[i]:
            read_s += 1
            if read_s == len(s):
                return True
        i += 1

    return False


print(is_subsequence(s="abc", t="ahbgdc"))
print(is_subsequence(s="axc", t="ahbgdc"))
