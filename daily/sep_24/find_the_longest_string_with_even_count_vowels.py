def find_the_longest_substring(s: str) -> int:
    vowels = set('aeiou')
    mask = 0
    res = 0

    mask_to_index = {0: -1}

    for i, c in enumerate(s):
        if c in vowels:
            mask = mask ^ (1 + ord(c) - ord('a'))
        if mask in mask_to_index:
            length = i - mask_to_index[mask]
            res = max(res, length)
        else:
            mask_to_index[mask] = i

    return res


print(find_the_longest_substring('eleetminicoworoep'))
print(find_the_longest_substring('leetcodeisgreat'))
print(find_the_longest_substring('bcbcbc'))

# Example 1:
#
# Input: s = "eleetminicoworoep"
# Output: 13
# Explanation: The longest substring is "leetminicowor" which contains two
# each of the vowels: e, i and o and zero of the vowels: a and u.
#
# Example 2:
#
# Input: s = "leetcodeisgreat"
# Output: 5
# Explanation: The longest substring is "leetc" which contains two e's.

# Example 3:
#
# Input: s = "bcbcbc"
# Output: 6 Explanation: In this case, the given string "bcbcbc" is the longest because all
# vowels: a, e, i, o and u appear zero times.
