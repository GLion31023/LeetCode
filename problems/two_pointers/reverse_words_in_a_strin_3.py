def reverse_words(s: str) -> str:
    word = list(s)
    left, right = 0, 0

    while right < len(word):
        if word[right] == ' ' or right == len(word) - 1:
            end = right if word[right] == ' ' else right + 1

            i, j = left, end - 1
            while i < j:
                word[i], word[j] = word[j], word[i]
                i += 1
                j -= 1

            left = right + 1

        right += 1

    return "".join(word)


print(reverse_words("Let's take LeetCode contest"))
print(reverse_words("Mr Ding"))
print(reverse_words("I love u"))

# Example 1:
#
# Input: s = "Let's take LeetCode contest"
# Output: "s'teL ekat edoCteeL tsetnoc"

# Example 2:
#
# Input: s = "Mr Ding"
# Output: "rM gniD"
