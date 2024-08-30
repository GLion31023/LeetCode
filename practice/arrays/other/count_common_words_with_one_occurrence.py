from collections import defaultdict


def count_cmn_words(words1: list[str], words2: list[str]) -> int:
    result = 0

    count1 = defaultdict(int)
    count2 = defaultdict(int)

    for w in words1:
        count1[w] += 1

    for w in words2:
        count2[w] += 1

    for k, v in count1.items():
        if v == 1 and count2[k] == 1:
            result += 1

    return result


print(count_cmn_words(words1=["leetcode", "is", "amazing", "as", "is"], words2=["amazing", "leetcode", "is"]))
print(count_cmn_words(words1=["b", "bb", "bbb"], words2=["a", "aa", "aaa"]))
print(count_cmn_words(words1=["a", "ab"], words2=["a", "a", "a", "ab"]))
