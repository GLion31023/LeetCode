def first_palindrome(words: list[str]) -> str:
    for w in words:
        if w == w[::-1]:
            return w

    return ""
    # for w in words:
    #     s, e = 0, len(w) - 1
    #
    #     while s <= e:
    #         if w[s] != w[e]:
    #             break
    #         s += 1
    #         e -= 1
    #         if e < s:
    #             return w
    #
    # return ""


print(first_palindrome(words=["abc", "car", "ada", "racecar", "cool"]))
print(first_palindrome(["notapalindrome", "racecar"]))
print(first_palindrome(["def", "ghi"]))
print(first_palindrome(["def", "ghi", "e"]))


# Example 1:
#
# Input: words = ["abc","car","ada","racecar","cool"]
# Output: "ada"
# Explanation: The first string that is palindromic is "ada".
# Note that "racecar" is also palindromic, but it is not the first.

# Example 2:
#
# Input: words = ["notapalindrome","racecar"]
# Output: "racecar"
# Explanation: The first and only string that is palindromic is "racecar".

# Example 3:
#
# Input: words = ["def","ghi"]
# Output: ""
# Explanation: There are no palindromic strings, so the empty string is returned.
