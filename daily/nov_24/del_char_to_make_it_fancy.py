def make_fancy_str(s: str) -> str:
    result = s[0]
    count = 1

    for c in s[1:]:
        if c != result[-1]:
            count = 1
            result += c
        else:
            if count == 2:
                continue
            count += 1
            result += c

    return result


print(make_fancy_str("leeetcode"))
print(make_fancy_str("aaabaaaa"))
print(make_fancy_str("aab"))

# Example 1:
# Input: s = "leeetcode"
# Output: "leetcode"
# Explanation:
# Remove an 'e' from the first group of 'e's to create "leetcode".
# No three consecutive characters are equal, so return "leetcode".

# Example 2:
# Input: s = "aaabaaaa"
# Output: "aabaa"
# Explanation:
# Remove an 'a' from the first group of 'a's to create "aabaaaa".
# Remove two 'a's from the second group of 'a's to create "aabaa".
# No three consecutive characters are equal, so return "aabaa".

# Example 3:
# Input: s = "aab"
# Output: "aab"
# Explanation: No three consecutive characters are equal, so return "aab".
