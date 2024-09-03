def get_longest_subsequence(words: list[str], groups: list[int]) -> list[str]:
    result = [words[0]]

    for i in range(len(groups) - 1):
        if groups[i] != groups[i + 1]:
            result.append(words[i + 1])

    return result


print(get_longest_subsequence(words=["e", "a", "b"], groups=[0, 0, 1]))
print(get_longest_subsequence(words=["a", "b", "c", "d"], groups=[1, 0, 1, 1]))
print(get_longest_subsequence(words=["d"], groups=[1]))
print(get_longest_subsequence(words=["c"], groups=[0]))
print(get_longest_subsequence(words=["c", "d"], groups=[0, 1]))
print(get_longest_subsequence(words=["c", "d"], groups=[1, 1]))
print(get_longest_subsequence(words=["tu", "rv", "bn"], groups=[0, 0, 0]))
print(get_longest_subsequence(words=["lr", "h"], groups=[0, 0]))
