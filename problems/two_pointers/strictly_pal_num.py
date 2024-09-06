def strictly_pal_num(n: int) -> bool:
    for b in range(2, n - 1):
        num = n
        b_rep = ""

        while num:
            rem = num % b
            b_rep = str(rem) + b_rep
            num //= b

        s, e = 0, len(b_rep) - 1

        while s < e:
            if b_rep[s] != b_rep[e]:
                return False
            s += 1
            e -= 1

    return True


print(strictly_pal_num(9))
print(strictly_pal_num(4))

# Example 1:
#
# Input: n = 9
# Output: false
# Explanation: In base 2: 9 = 1001 (base 2), which is palindromic.
# In base 3: 9 = 100 (base 3), which is not palindromic.
# Therefore, 9 is not strictly palindromic so we return false.
# Note that in bases 4, 5, 6, and 7, n = 9 is also not palindromic.

# Example 2:
#
# Input: n = 4
# Output: false
# Explanation: We only consider base 2: 4 = 100 (base 2), which is not palindromic.
# Therefore, we return false.
