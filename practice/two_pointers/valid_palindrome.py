def is_palindrome(s: str) -> bool:
    left, right = 0, len(s) - 1

    def is_alphanum(char):
        return (ord("A") <= ord(char) <= ord("Z") or
                ord("a") <= ord(char) <= ord("z") or
                ord("0") <= ord(char) <= ord("9"))

    while left < right:
        while left < right and not is_alphanum(s[left]):
            left += 1

        while right > left and not is_alphanum(s[right]):
            right -= 1

        if s[left].lower() != s[right].lower():
            return False
        left, right = left + 1, right - 1

    return True


print(is_palindrome("Was it a car or a cat I saw?"))
print(is_palindrome("tab a cat"))
print(is_palindrome("Able was I, ere I saw Elba"))
print(is_palindrome(s=" "))
