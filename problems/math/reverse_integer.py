def reverse_int(x: int) -> int:
    max_32bit_int = 2 ** 31
    sign = 1
    str_int = str(x)

    if x < 0:
        sign *= -1
        str_int = str_int[1:]

    rev_int = int(str_int[::-1]) * sign

    if rev_int < max_32bit_int * (-1) or max_32bit_int - 1 < rev_int:
        return 0

    return rev_int


print(reverse_int(123))
print(reverse_int(-123))
print(reverse_int(120))
print(reverse_int(1534236469))

# Example 1:
# Input: x = 123
# Output: 321

# Example 2:
# Input: x = -123
# Output: -321

# Example 3:
# Input: x = 120
# Output: 21
