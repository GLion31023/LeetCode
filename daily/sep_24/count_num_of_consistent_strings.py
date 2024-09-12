def count_consistent_strings(allowed: str, words: list[str]) -> int:
    allowed_c = set(allowed)
    consistent = 0

    for w in words:
        is_allowed = True
        for c in w:
            if c not in allowed_c:
                is_allowed = False
                break
        if is_allowed:
            consistent += 1

    return consistent


print(count_consistent_strings(allowed="ab", words=["ad", "bd", "aaab", "baa", "badab"]))
print(count_consistent_strings(allowed="abc", words=["a", "b", "c", "ab", "ac", "bc", "abc"]))
print(count_consistent_strings(allowed="cad", words=["cc", "acd", "b", "ba", "bac", "bad", "ac", "d"]))

# Example 1:
#
# Input: allowed = "ab", words = ["ad","bd","aaab","baa","badab"]
# Output: 2
# Explanation: Strings "aaab" and "baa" are consistent since they only contain characters 'a' and 'b'.

# Example 2:
#
# Input: allowed = "abc", words = ["a","b","c","ab","ac","bc","abc"]
# Output: 7
# Explanation: All strings are consistent.

# Example 3:
#
# Input: allowed = "cad", words = ["cc","acd","b","ba","bac","bad","ac","d"]
# Output: 4
# Explanation: Strings "cc", "acd", "ac", and "d" are consistent.
