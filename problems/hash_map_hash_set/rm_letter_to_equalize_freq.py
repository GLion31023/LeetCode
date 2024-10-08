import copy


def equal_frequency(word: str) -> bool:
    freq_arr = [0] * 26
    base_ord = ord('a')

    for c in word:
        pos = ord(c) - base_ord
        freq_arr[pos] += 1

    freq_map = [x for x in freq_arr if x != 0]

    for c in range(len(freq_map)):
        map_copy = copy.deepcopy(freq_map)
        map_copy[c] -= 1

        if map_copy[c] == 0:
            del map_copy[c]

        if len(set(map_copy)) == 1:
            return True

    return False


print(equal_frequency("abcc"))
print(equal_frequency("aazz"))
print(equal_frequency("bac"))
print(equal_frequency("abbcc"))
print(equal_frequency("ddaccb"))
print(equal_frequency("cccaa"))

# Example 1:
# Input: word = "abcc"
# Output: true
# Explanation: Select index 3 and delete it: word becomes "abc" and each character has a frequency of 1.

# Example 2: Input: word = "aazz" Output: false Explanation: We must delete a character, so either the frequency of
# "a" is 1 and the frequency of "z" is 2, or vice versa. It is impossible to make all present letters have equal
# frequency.
