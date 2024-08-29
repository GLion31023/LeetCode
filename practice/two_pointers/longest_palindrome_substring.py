def longest_palindrome_substring(s: str) -> str:
    res_l, res_r = 0, 0

    for i in range(len(s)):
        left, right = i, i
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        if (right - left - 1) > (res_r - res_l):
            res_l, res_r = left + 1, right

        left, right = i, i + 1
        while 0 <= left and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        if (right - left - 1) > (res_r - res_l):
            res_l, res_r = left + 1, right

    return s[res_l:res_r]


print(longest_palindrome_substring(s="babad"))
print(longest_palindrome_substring(s="cbbd"))
