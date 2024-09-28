def my_atoi(s: str) -> int:
    s = s.strip()
    if not s:
        return 0

    length = len(s)
    max_32bit_int = 2 ** 31
    i = res = 0
    sign = 1

    if s[i] == "-":
        sign = -1
        i += 1
    elif s[i] == '+':
        i += 1

    if i == length or not s[i].isdigit():
        return 0

    while s[i].isdigit() and i < length:
        curr_n = s[i]
        i += 1
        res = res * 10 + int(curr_n)
        if res >= max_32bit_int:
            if sign > 0:
                return max_32bit_int - sign
            else:
                return max_32bit_int * sign
        if i == length:
            break

    return res * sign


print(my_atoi('42'))
print(my_atoi(' -042'))
print(my_atoi('1337c0d3'))
print(my_atoi('0-1'))
print(my_atoi('words and 987'))
print(my_atoi("-91283472332"))
print(my_atoi("-"))
print(my_atoi("21474836460"))


# Example 1:
# Input: s = "42"
# Output: 42
# Explanation:
# The underlined characters are what is read in and the caret is the current reader position.
# Step 1: "42" (no characters read because there is no leading whitespace)    ^
# Step 2: "42" (no characters read because there is neither a '-' nor '+')
# Step 3: "42" ("42" is read in)
#            ^
# Example 2:
# Input: s = " -042"
# Output: -42
# Explanation:
# Step 1: "   -042" (leading whitespace is read and ignored)   ^
# Step 2: "   -042" ('-' is read, so the result should be negative)     ^
# Step 3: "   -042" ("042" is read in, leading zeros ignored in the result)
#                ^
# Example 3:
# Input: s = "1337c0d3"
# Output: 1337
# Explanation:
# Step 1: "1337c0d3" (no characters read because there is no leading whitespace)   ^
# Step 2: "1337c0d3" (no characters read because there is neither a '-' nor '+')  ^
# Step 3: "1337c0d3" ("1337" is read in; reading stops because the next character is a non-digit)
#              ^
# Example 4:
# Input: s = "0-1"
# Output: 0
# Explanation:
# Step 1: "0-1" (no characters read because there is no leading whitespace)
# Step 2: "0-1" (no characters read because there is neither a '-' nor '+')
# Step 3: "0-1" ("0" is read in; reading stops because the next character is a non-digit)
#           ^
# Example 5:
# Input: s = "words and 987"
# Output: 0
# Explanation:
# Reading stops at the first non-digit character 'w'.
