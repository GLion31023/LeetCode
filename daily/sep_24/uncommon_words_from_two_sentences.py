def uncommon_words(s1: str, s2: str) -> list[str]:
    # this solution performed better
    result = []
    seen = set()
    set1 = set(s1.split())
    set2 = set(s2.split())
    
    for w in s1.split():
        if w not in set2 and w not in seen:
            result.append(w)
            seen.add(w)
        elif w in seen and w in result:
            result.remove(w)

    for w in s2.split():
        if w not in set1 and w not in seen:
            result.append(w)
            seen.add(w)
        elif w in seen and w in result:
            result.remove(w)

    return result

    # s1 = s1.split()
    # s2 = s2.split()
    # set1 = set(s1)
    # set2 = set(s2)
    #
    # result = []
    #
    # for w in set1:
    #     if w not in set2 and s1.count(w) == 1:
    #         result.append(w)
    #
    # for w in set2:
    #     if w not in set1 and s2.count(w) == 1:
    #         result.append(w)
    #
    # return result


print(uncommon_words("this apple is sweet", "this apple is sour"))
print(uncommon_words("apple apple", "banana"))
print(uncommon_words("s z z z s", "s z ejt"))
print(uncommon_words("xfj vcahm vcahm frkqt oibcc jko oibcc frkqt ft tr",
                     "lv ktx ktx tr x xfj xfj frkqt ktx ta tr yynk vcahm"))

# Example 1:
#
# Input: s1 = "this apple is sweet", s2 = "this apple is sour"
# Output: ["sweet","sour"]
# Explanation:
# The word "sweet" appears only in s1, while the word "sour" appears only in s2.
#
# Example 2:
# Input: s1 = "apple apple", s2 = "banana"
# Output: ["banana"]
