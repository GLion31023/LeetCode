from functools import cache


def extra_char_in_str(s: str, dictionary: list[str]) -> int:
    dictionary = set(dictionary)

    @cache
    def dfs(i):
        if i == len(s):
            return 0

        result = 1 + dfs(i + 1)
        for r in range(i, len(s) + 1):
            if s[i:r] in dictionary:
                result = min(result, dfs(r))

        return result

    return dfs(0)


print(extra_char_in_str("leetscode", ["leet", "code", "leetcode"]))
print(extra_char_in_str("sayhelloworld", ["hello", "world"]))
print(extra_char_in_str("dwmodizxvvbosxxw", ["ox", "lb", "diz", "gu", "v", "ksv", "o", "nuq", "r", "txhe", "e", "wmo",
                                             "cehy", "tskz", "ds", "kzbu"]))

# Example 1:
#
# Input: s = "leetscode", dictionary = ["leet","code","leetcode"]
# Output: 1
# Explanation: We can break s in two substrings: "leet" from index 0 to 3 and "code" from index 5 to 8. There is only 1
# unused character (at index 4), so we return 1.
#
# Example 2:
#
# Input: s = "sayhelloworld", dictionary = ["hello","world"]
# Output: 3
# Explanation: We can break s in two substrings: "hello" from index 3 to 7 and "world" from index 8 to 12.
# The characters at indices 0, 1, 2 are not used in any substring and thus are considered as extra characters.
# Hence, we return 3.
