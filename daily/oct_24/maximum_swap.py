def max_swap(num: int) -> int:
    num_str = list(str(num))
    order = [-1 for _ in range(10)]

    for i, digit in enumerate(num_str):
        n = int(digit)
        order[n] = i

    for i, digit in enumerate(num_str):
        curr_digit = int(digit)

        for d in range(9, curr_digit, -1):
            if order[d] > i:
                num_str[i], num_str[order[d]] = num_str[order[d]], num_str[i]
                return int(''.join(num_str))

    return num


print(max_swap(2736))
print(max_swap(9973))
print(max_swap(98800435))

# Example 1:
# Input: num = 2736
# Output: 7236
# Explanation: Swap the number 2 and the number 7.

# Example 2:
# Input: num = 9973
# Output: 9973
# Explanation: No swap.
