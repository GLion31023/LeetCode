def replace_chalk(chalk: list[int], k: int) -> int:
    k %= sum(chalk)

    for i in range(len(chalk)):
        if k < chalk[i]:
            return i
        k -= chalk[i]


print(replace_chalk(chalk=[5, 1, 5], k=22))
print(replace_chalk(chalk=[3, 4, 1, 2], k=25))

# Example 1:
#
# Input: chalk = [5,1,5], k = 22
# Output: 0
# Explanation: The students go in turns as follows:
# - Student number 0 uses 5 chalk, so k = 17.
# - Student number 1 uses 1 chalk, so k = 16.
# - Student number 2 uses 5 chalk, so k = 11.
# - Student number 0 uses 5 chalk, so k = 6.
# - Student number 1 uses 1 chalk, so k = 5.
# - Student number 2 uses 5 chalk, so k = 0.
# Student number 0 does not have enough chalk, so they will have to replace it.

# Example 2:
#
# Input: chalk = [3,4,1,2], k = 25
# Output: 1
# Explanation: The students go in turns as follows:
# - Student number 0 uses 3 chalk so k = 22.
# - Student number 1 uses 4 chalk so k = 18.
# - Student number 2 uses 1 chalk so k = 17.
# - Student number 3 uses 2 chalk so k = 15.
# - Student number 0 uses 3 chalk so k = 12.
# - Student number 1 uses 4 chalk so k = 8.
# - Student number 2 uses 1 chalk so k = 7.
# - Student number 3 uses 2 chalk so k = 5.
# - Student number 0 uses 3 chalk so k = 2.
# Student number 1 does not have enough chalk, so they will have to replace it.