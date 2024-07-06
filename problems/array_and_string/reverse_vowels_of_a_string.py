def reverse_vowels(s: str) -> str:
    left, right = 0, len(s) - 1
    vowels = set("aeiouAEIOU")
    result = list(s)

    while left < right:
        if result[left] in vowels and result[right] in vowels:
            result[left], result[right] = result[right], result[left]
            left += 1
            right -= 1
        if result[left] not in vowels:
            left += 1
        if result[right] not in vowels:
            right -= 1

    return "".join(result)


print(reverse_vowels("hello"))
print(reverse_vowels("leetcode"))
