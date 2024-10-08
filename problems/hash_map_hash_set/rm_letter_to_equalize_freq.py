def equal_frequency(word: str) -> bool:
    freq_arr = [0] * 26
    base_ord = ord('a')

    for c in word:
        pos = ord(c) - base_ord
        freq_arr[pos] += 1

    freqs = sorted([x for x in freq_arr if x != 0])

    if freqs[0] == 1 and freqs[-1] == 1:
        return True

    h = freqs[-1]
    l = freqs[0]

    if 0 < l - 1 == h:
        n = l - 1
        for i in freqs[1:]:
            if i != n:
                return False
    elif 0 == l - 1 and freqs[1] == h:
        n = freqs[1]
        for i in freqs[2:]:
            if i != n:
                return False
    else:
        n = h - 1
        freqs[-1] = n
        for i in freqs:
            if i != n:
                return False

    return True

    # seen = defaultdict(int)
    #
    # for c in word:
    #     seen[c] += 1
    #
    # max_freq = max(seen.items(), key=operator.itemgetter(1))[0]
    # seen[max_freq] -= 1
    # val = seen[max_freq]
    # if val == 0:
    #     del seen[max_freq]
    #
    # f_Val = None
    # for v in seen.values():
    #     f_Val = v
    #     break
    #
    # return sum(seen.values()) / len(seen) == f_Val


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
