def is_palindrome(s: str) -> bool:
    s = s.lower()
    s = "".join([i for i in s if i.isalnum()])
    return s == s[::-1]


print(is_palindrome("A man, a plan, a canal: Panama"))
print(is_palindrome("race a car"))
print(is_palindrome(""))
print(is_palindrome("0P"))
