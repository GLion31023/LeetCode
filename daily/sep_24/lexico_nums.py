from collections import defaultdict


def lexical_order(n: int) -> list[int]:
    num = 1
    result = [0] * n

    for i in range(n):
        result[i] = num
        if num * 10 <= n:
            num *= 10
        else:
            if num == n:
                num //= 10
            num += 1
            while num % 10 == 0:
                num //= 10

    return result


print(lexical_order(10001))

# Example 1:
#
# Input: n = 13
# Output: [1,10,11,12,13,2,3,4,5,6,7,8,9]

# Example 2:
#
# Input: n = 2
# Output: [1,2]
