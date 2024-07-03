def merge_alternately(word1: str, word2: str) -> str:
    res = ''
    min_len = min(len(word1), len(word2))

    for i in range(min_len):
        res += word1[i] + word2[i]

    if len(word1) > min_len:
        res += word1[min_len:]
    else:
        res += word2[min_len:]

    return res


print(merge_alternately(word1="abc", word2="pqr"))
print(merge_alternately(word1="ab", word2="pqrs"))
print(merge_alternately(word1="abcd", word2="pq"))
