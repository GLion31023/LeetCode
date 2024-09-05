def find_missing_observations(rolls: list[int], mean: int, n: int) -> list[int]:
    sum_n = mean * (len(rolls) + n) - sum(rolls)

    avg_n = sum_n // n
    rem = sum_n % n

    if sum_n > 6 * n or sum_n < n:
        return []

    result = [avg_n] * n
    for i in range(rem):
        result[i] += 1

    return result


print(find_missing_observations(rolls=[3, 2, 4, 3], mean=4, n=2))
print(find_missing_observations(rolls=[3, 1, 4, 3], mean=4, n=2))
print(find_missing_observations(rolls=[1, 5, 6], mean=3, n=4))
print(find_missing_observations(rolls=[1, 2, 3, 4], mean=6, n=4))
print(find_missing_observations([6, 3, 4, 3, 5, 3], 1, 6))
print(find_missing_observations(
    [4, 5, 6, 2, 3, 6, 5, 4, 6, 4, 5, 1, 6, 3, 1, 4, 5, 5, 3, 2, 3, 5, 3, 2, 1, 5, 4, 3, 5, 1, 5], 4, 40))

# Example 1:
#
# Input: rolls = [3,2,4,3], mean = 4, n = 2
# Output: [6,6]
# Explanation: The mean of all n + m rolls is (3 + 2 + 4 + 3 + 6 + 6) / 6 = 4.

# Example 2:
#
# Input: rolls = [1,5,6], mean = 3, n = 4
# Output: [2,3,2,2]
# Explanation: The mean of all n + m rolls is (1 + 5 + 6 + 2 + 3 + 2 + 2) / 7 = 3.

# Example 3:
#
# Input: rolls = [1,2,3,4], mean = 6, n = 4
# Output: []
# Explanation: It is impossible for the mean to be 6 no matter what the 4 missing rolls are.
