def count_bits(n: int) -> list[int]:
    res = []

    for n in range(n + 1):
        res.append(n.bit_count())

    return res


print(count_bits(2))
print(count_bits(5))


# Example 1:
# Input: n = 2
# Output: [0,1,1]
# Explanation:
# 0 --> 0
# 1 --> 1
# 2 --> 10

# Example 2:
# Input: n = 5
# Output: [0,1,1,2,1,2]
# Explanation:
# 0 --> 0
# 1 --> 1
# 2 --> 10
# 3 --> 11
# 4 --> 100
# 5 --> 101
