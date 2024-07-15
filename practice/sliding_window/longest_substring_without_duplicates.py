def length_of_longest_substring(s: str) -> int:
    longest = 0
    left = 0
    seen = set()

    for right in range(len(s)):
        while s[right] in seen:
            seen.remove(s[left])
            left += 1
        seen.add(s[right])
        longest = max(longest, right - left + 1)

    return longest


print(length_of_longest_substring("zxyzxyz"))
print(length_of_longest_substring("xxxx"))
print(length_of_longest_substring("abcabcbb"))
print(length_of_longest_substring("pwwkew"))
print(length_of_longest_substring("dvdf"))
