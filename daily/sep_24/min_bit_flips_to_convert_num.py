def min_bit_flips(start: int, goal: int) -> int:
    a, b = bin(start)[2:], bin(goal)[2:]
    diff = abs(len(a) - len(b))

    if len(a) < len(b):
        a = '0' * diff + a
    else:
        b = '0' * diff + b

    flips = 0

    for i in range(len(a)):
        if a[i] != b[i]:
            flips += 1

    return flips


# bin(start ^ goal).count('1')
# (start ^ goal).bit_count()

print(min_bit_flips(10, 7))
print(min_bit_flips(3, 4))
print(min_bit_flips(99, 29))
print(min_bit_flips(10, 82))

# Example 1:
#
# Input: start = 10, goal = 7
# Output: 3
# Explanation: The binary representation of 10 and 7 are 1010 and 0111 respectively. We can convert 10 to 7 in 3 steps:
# - Flip the first bit from the right: 1010 -> 1011.
# - Flip the third bit from the right: 1011 -> 1111.
# - Flip the fourth bit from the right: 1111 -> 0111.
# It can be shown we cannot convert 10 to 7 in less than 3 steps. Hence, we return 3.

# Example 2:
#
# Input: start = 3, goal = 4
# Output: 3
# Explanation: The binary representation of 3 and 4 are 011 and 100 respectively. We can convert 3 to 4 in 3 steps:
# - Flip the first bit from the right: 011 -> 010.
# - Flip the second bit from the right: 010 -> 000.
# - Flip the third bit from the right: 000 -> 100.
# It can be shown we cannot convert 3 to 4 in less than 3 steps. Hence, we return 3.
