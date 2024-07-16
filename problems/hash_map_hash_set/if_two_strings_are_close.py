def close_strings(word1: str, word2: str) -> bool:
    if len(word1) != len(word2):
        return False

    chars = {}
    chars2 = {}

    for c in word1:
        chars[c] = chars.get(c, 0) + 1

    for c in word2:
        chars2[c] = chars2.get(c, 0) + 1

    if set(chars.keys()) != set(chars2.keys()):
        return False

    if sorted(chars.values()) != sorted(chars2.values()):
        return False

    return True


print(close_strings("abc", word2="bca"))
print(close_strings("a", word2="aa"))
print(close_strings("cabbba", word2="abbccc"))
print(close_strings("uau", word2="ssx"))
print(close_strings("aaabbbbccddeeeeefffff", word2="aaaaabbcccdddeeeeffff"))
