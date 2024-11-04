def compress_string(word: str) -> str:
    comp = ''
    char = word[0]
    count = 1

    for c in word[1:]:
        if c != char or count == 9:
            comp += str(count) + char
            char = c
            count = 1
        else:
            count += 1

    comp += str(count) + char

    return comp


print(compress_string("abcde"))
print(compress_string("aaaaaaaaaaaaaabb"))


# Example 1: Input: word = "abcde"
# Output: "1a1b1c1d1e"
# Explanation: Initially, comp = "". Apply the operation 5
# times, choosing "a", "b", "c", "d", and "e" as the prefix in each operation. For each prefix, append "1" followed
# by the character to comp.
#
# Example 2: Input: word = "aaaaaaaaaaaaaabb"
# Output: "9a5a2b"
# Explanation: Initially, comp = "". Apply the operation
# 3 times, choosing "aaaaaaaaa", "aaaaa", and "bb" as the prefix in each operation. For prefix "aaaaaaaaa",
# append "9" followed by "a" to comp. For prefix "aaaaa", append "5" followed by "a" to comp. For prefix "bb",
# append "2" followed by "b" to comp.
