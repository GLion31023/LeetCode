def is_circular(sentence: str) -> bool:
    words = sentence.split()
    first = words[0]

    if len(words) == 1:
        return first[0] == first[-1]

    for i in words[1:]:
        if first[-1] != i[0]:
            return False
        first = i

    return words[-1][-1] == words[0][0]


print(is_circular("leetcode exercises sound delightful"))
print(is_circular("eetcode"))
print(is_circular("Leetcode is cool"))


# Example 1:
# Input: sentence = "leetcode exercises sound delightful"
# Output: true
# Explanation: The words in sentence are ["leetcode", "exercises", "sound", "delightful"].
# - leetcode's last character is equal to exercises's first character.
# - exercises's last character is equal to sound's first character.
# - sound's last character is equal to delightful's first character.
# - delightful's last character is equal to leetcode's first character.
# The sentence is circular.

# Example 2:
# Input: sentence = "eetcode"
# Output: true
# Explanation: The words in sentence are ["eetcode"].
# - eetcode's last character is equal to eetcode's first character.
# The sentence is circular.

# Example 3:
# Input: sentence = "Leetcode is cool"
# Output: false
# Explanation: The words in sentence are ["Leetcode", "is", "cool"].
# - Leetcode's last character is not equal to is's first character.
# The sentence is not circular.
