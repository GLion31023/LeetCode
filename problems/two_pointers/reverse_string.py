def reverseString(s: list[str]) -> None:
    """
    Do not return anything, modify s in-place instead.
    """
    start, end = 0, len(s) - 1
    while start < end:
        s[start], s[end] = s[end], s[start]
        start += 1
        end -= 1


s = ["h", "e", "l", "l", "o"]
reverseString(s)
print(s)


# Example 1:
# Input: s = ["h","e","l","l","o"]
# Output: ["o","l","l","e","h"]

# Example 2:
# Input: s = ["H","a","n","n","a","h"]
# Output: ["h","a","n","n","a","H"]
