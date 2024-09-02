def max_num_of_str_pairs(words: list[str]) -> int:
    active_pairs = set()
    pairs = 0

    for w in words:
        if w in active_pairs:
            pairs += 1
            active_pairs.remove(w)
        else:
            active_pairs.add(w[::-1])

    return pairs


print(max_num_of_str_pairs(["cd", "ac", "dc", "ca", "zz"]))
print(max_num_of_str_pairs(["ab", "ba", "cc"]))
print(max_num_of_str_pairs(["aa", "ab"]))
