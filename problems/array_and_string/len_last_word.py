def len_last_word(s: str) -> int:
    s = s.strip()
    length_last = 0

    for c in s:
        if c.isalpha():
            length_last += 1
        else:
            length_last = 0

    return length_last


print(len_last_word("Hello World"))
print(len_last_word("   fly me   to   the moon  "))
print(len_last_word("luffy is still joyboy"))

# Example 1
# Input: s = "Hello World"
# Output: 5
# Explanation: The last word is "World" with length 5.

# Example 2:
# Input: s = "   fly me   to   the moon  "
# Output: 4
# Explanation: The last word is "moon" with length 4.

# Example 3:
# Input: s = "luffy is still joyboy"
# Output: 6
# Explanation: The last word is "joyboy" with length 6.
