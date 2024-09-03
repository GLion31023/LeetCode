from collections import defaultdict


def max_pal_after_operations(words: list[str]) -> int:
    chars = defaultdict(int)
    len_words = []
    max_num_of_pals = 0

    for w in words:
        len_words.append(len(w))
        for c in w:
            chars[c] += 1

    len_words.sort(reverse=False)
    single_chars_sum = 0
    even_chars_sum = 0

    for v in chars.values():
        if v % 2 == 0:
            even_chars_sum += v
        else:
            single_chars_sum += 1
            if v > 1:
                even_chars_sum += (v - 1)

    for l in len_words:
        if l % 2 == 0:
            if even_chars_sum >= l:
                even_chars_sum -= l
                max_num_of_pals += 1
        else:
            if l > 2:
                single_chars_sum -= 1
                if even_chars_sum >= l - 1:
                    even_chars_sum -= (l - 1)
                    max_num_of_pals += 1
            else:
                single_chars_sum -= 1
                max_num_of_pals += 1

    return max_num_of_pals


print(max_pal_after_operations(["abbb", "ba", "aa"]))
print(max_pal_after_operations(["abc", "ab"]))
print(max_pal_after_operations(["cd", "ef", "a"]))
print(max_pal_after_operations(["a", "ccc"]))
print(max_pal_after_operations(["rqfsx", "kja", "mx", "r"]))
