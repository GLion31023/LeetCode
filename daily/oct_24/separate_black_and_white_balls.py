def min_steps(s: str) -> int:
    steps = 0
    pos = 0

    for i in range(len(s)):
        if s[i] == '0':
            steps += i - pos
            pos += 1

    return steps


print(min_steps("101"))
print(min_steps("00"))
print(min_steps("100"))
print(min_steps("0111"))
print(min_steps("0011000010"))
print(min_steps("111111111111111111111111111111111111111110011"))
print(min_steps("1111110000000000000000000000000000000000001011"))

# Example 1:
# Input: s = "101"
# Output: 1
# Explanation: We can group all the black balls to the right in the following way:
# - Swap s[0] and s[1], s = "011".
# Initially, 1s are not grouped together, requiring at least 1 step to group them to the right.

# Example 2:
# Input: s = "100"
# Output: 2
# Explanation: We can group all the black balls to the right in the following way:
# - Swap s[0] and s[1], s = "010".
# - Swap s[1] and s[2], s = "001".
# It can be proven that the minimum number of steps needed is 2.

# Example 3:
# Input: s = "0111"
# Output: 0
# Explanation: All the black balls are already grouped to the right.
