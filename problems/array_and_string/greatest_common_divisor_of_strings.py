def gcd_of_strings(str1: str, str2: str) -> str:
    l1, l2 = len(str1), len(str2)

    if str1 + str2 != str2 + str1:
        return ""

    while l2 != 0:
        l1, l2 = l2, l1 % l2

    return str1[:l1]


print(gcd_of_strings("ABCABC", "ABC"))
print(gcd_of_strings("ABABAB", "ABAB"))
print(gcd_of_strings("LEET", "CODE"))
print(gcd_of_strings("ABCDEF", "ABC"))
print(gcd_of_strings("AAAAAAAAA", "AAACCC"))
print(gcd_of_strings("TAUXXTAUXXTAUXXTAUXXTAUXX", "TAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXX"))
