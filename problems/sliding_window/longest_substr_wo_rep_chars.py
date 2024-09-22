def len_of_longest_substr(s: str) -> int:
    left, right = 0, 0
    max_substr = 0
    seen = set()
    length = len(s)

    while right < length:
        if s[right] not in seen:
            seen.add(s[right])
            max_substr = max(max_substr, right - left + 1)
            right += 1
        else:
            seen.remove(s[left])
            left += 1

    return max_substr


print(len_of_longest_substr('abcabcbb'))
print(len_of_longest_substr('bbbbb'))
print(len_of_longest_substr('pwwkew'))
print(len_of_longest_substr('au'))
print(len_of_longest_substr('dvdf'))

# Example 1:
# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.
#
# Example 2:
# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
#
# Example 3:
# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring
