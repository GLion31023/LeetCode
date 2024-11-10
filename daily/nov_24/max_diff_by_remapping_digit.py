def min_max_diff(num: int) -> int:
    maxi = num
    mini = num
    s_n = str(num)

    for n in s_n:
        if n != "9":
            maxi = int(s_n.replace(n, '9'))
            break

    for n in s_n:
        if n != "0":
            mini = int(s_n.replace(n, '0'))

        return maxi - mini


print(min_max_diff(11891))
print(min_max_diff(90))
print(min_max_diff(99999))
print(min_max_diff(456))

# Example 1:
# Input: num = 11891
# Output: 99009
# Explanation:
# To achieve the maximum value, Bob can remap the digit 1 to the digit 9 to yield 99899.
# To achieve the minimum value, Bob can remap the digit 1 to the digit 0, yielding 890.
# The difference between these two numbers is 9900

# Example 2: Input: num = 90 Output: 99 Explanation: The maximum value that can be returned by the function is 99 (if
# 0 is replaced by 9) and the minimum value that can be returned by the function is 0 (if 9 is replaced by 0). Thus,
# we return 99.
