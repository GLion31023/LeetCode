def check_inclusion(s1: str, s2: str) -> bool:
    len_s1 = len(s1)
    len_s2 = len(s2)

    if len_s1 > len_s2:
        return False

    s1_freq = [0] * 26
    wind_freq = [0] * 26
    base_char = ord('a')

    for c in s1:
        s1_freq[ord(c) - base_char] += 1

    for c in s2[:len_s1]:
        wind_freq[ord(c) - base_char] += 1

    if s1_freq == wind_freq:
        return True

    for i in range(len_s1, len_s2):
        wind_freq[ord(s2[i]) - base_char] += 1
        wind_freq[ord(s2[i - len_s1]) - base_char] -= 1

        if s1_freq == wind_freq:
            return True

    return False


print(check_inclusion("ab", s2="eidbaooo"))
print(check_inclusion("ab", s2="eidboaoo"))
print(check_inclusion("hello", s2="ooolleoooleh"))
print(check_inclusion("adc", s2="dcda"))
