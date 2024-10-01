def longest_cmn_prefix(strs: list[str]) -> str:
    if not strs:
        return ""

    shortest = min(strs, key=len)
    prefix = ""

    for i, c in enumerate(shortest):
        for w in strs:
            if c != w[i]:
                return prefix

        prefix += c

    return prefix


print(longest_cmn_prefix(["flower", "flow", "flight"]))
print(longest_cmn_prefix(["dog", "racecar", "car"]))
print(longest_cmn_prefix(["reflower", "flow", "flight"]))
