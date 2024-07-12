def max_vowels(s: str, k: int) -> int:
    vowels = set('aeiou')
    max_vowels_s, curr_vowels = 0, 0

    for i in range(k):
        if s[i] in vowels:
            curr_vowels += 1

    max_vowels_s = curr_vowels

    for i in range(k, len(s)):
        if s[i] in vowels:
            curr_vowels += 1
        if s[i - k] in vowels:
            curr_vowels -= 1
        max_vowels_s = max(max_vowels_s, curr_vowels)

    return max_vowels_s


print(max_vowels("abciiidef", 3))
print(max_vowels("aeiou", 2))
print(max_vowels("leetcode", 3))
