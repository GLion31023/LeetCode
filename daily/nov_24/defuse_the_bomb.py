def defuse(code: list[int], k: int) -> list[int]:
    len_c = len(code)
    result = [0] * len_c

    if k == 0:
        return result

    elif k > 0:
        window_sum = sum(code[i % len_c] for i in range(1, k + 1))
        for i in range(len_c):
            result[i] = window_sum
            window_sum -= code[(i + 1) % len_c]
            window_sum += code[(i + k + 1) % len_c]
    else:
        k = abs(k)
        window_sum = sum(code[i % len_c] for i in range(-k, 0))
        for i in range(len_c):
            result[i] = window_sum
            window_sum -= code[(i - k) % len_c]
            window_sum += code[i % len_c]

    return result


print(defuse([5, 7, 1, 4], k=3))
print(defuse([1, 2, 3, 4], k=0))
print(defuse([2, 4, 9, 3], k=-2))

# Example 1:
# Input: code = [5,7,1,4], k = 3
# Output: [12,10,16,13]
# Explanation: Each number is replaced by the sum of the next 3 numbers.
# The decrypted code is [7+1+4, 1+4+5, 4+5+7, 5+7+1]. Notice that the numbers wrap around.

# Example 2:
# Input: code = [1,2,3,4], k = 0
# Output: [0,0,0,0]
# Explanation: When k is zero, the numbers are replaced by 0.

# Example 3:
# Input: code = [2,4,9,3], k = -2
# Output: [12,5,6,13]
# Explanation: The decrypted code is [3+9, 2+3, 4+2, 9+4]. Notice that the numbers wrap around again.
# If k is negative, the sum is of the previous numbers.
