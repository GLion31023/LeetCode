def convert_array(original: list[int], m: int, n: int) -> list[list[int]]:
    if len(original) != m * n:
        return []

    res = []

    for i in range(m):
        row = []
        for j in range(n):
            row.append(original[i * n + j])
        res.append(row)

    return res


print(convert_array(original=[1, 2, 3, 4], m=2, n=2))
print(convert_array(original=[1, 2, 3], m=1, n=3))
print(convert_array(original=[1, 2], m=1, n=1))
print(convert_array(original=[3], m=1, n=2))

# Example 1:
#
# Input: original = [1,2,3,4], m = 2, n = 2
# Output: [[1,2],[3,4]]
# Explanation: The constructed 2D array should contain 2 rows and 2 columns.
# The first group of n=2 elements in original, [1,2], becomes the first row in the constructed 2D array.
# The second group of n=2 elements in original, [3,4], becomes the second row in the constructed 2D array.

# Example 2:
#
# Input: original = [1,2,3], m = 1, n = 3
# Output: [[1,2,3]]
# Explanation: The constructed 2D array should contain 1 row and 3 columns.
# Put all three elements in original into the first row of the constructed 2D array.

# Example 3:
#
# Input: original = [1,2], m = 1, n = 1
# Output: []
# Explanation: There are 2 elements in original.
# It is impossible to fit 2 elements in a 1x1 2D array, so return an empty 2D array.
