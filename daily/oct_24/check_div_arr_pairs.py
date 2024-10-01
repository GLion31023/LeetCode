def can_arrange(arr: list[int], k: int) -> bool:
    count_rem = [0] * k

    for n in arr:
        rem = n % k
        if rem < 0:
            rem += k
        count_rem[rem] += 1

    if count_rem[0] % 2 != 0:
        return False

    for i in range(1, k):
        if count_rem[i] != count_rem[k - i]:
            return False

    return True


print(can_arrange(arr=[1, 2, 3, 4, 5, 10, 6, 7, 8, 9], k=5))
print(can_arrange(arr=[1, 2, 3, 4, 5, 6], k=7))
print(can_arrange(arr=[1, 2, 3, 4, 5, 6], k=10))
print(can_arrange(arr=[-1, 1, -2, 2, -3, 3, -4, 4], k=3))


# Example 1:
# Input: arr = [1,2,3,4,5,10,6,7,8,9], k = 5
# Output: true
# Explanation: Pairs are (1,9),(2,8),(3,7),(4,6) and (5,10).

# Example 2:
# Input: arr = [1,2,3,4,5,6], k = 7
# Output: true
# Explanation: Pairs are (1,6),(2,5) and(3,4).

# Example 3:
# Input: arr = [1,2,3,4,5,6], k = 10
# Output: false
# Explanation: You can try all possible pairs to see that there is no way to divide arr into 3 pairs
# each with sum divisible by 10.
