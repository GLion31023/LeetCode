import heapq


def largest_int(num: int) -> int:
    str_n = list(str(num))

    odds = [-int(n) for n in str_n if int(n) % 2 == 1]
    evens = [-int(n) for n in str_n if int(n) % 2 == 0]
    heapq.heapify(odds)
    heapq.heapify(evens)

    result = ''

    for i in range(len(str_n)):
        if int(str_n[i]) % 2 == 0:
            result += str(-heapq.heappop(evens))
        else:
            result += str(-heapq.heappop(odds))

    return int("".join(result))


print(largest_int(1234))
print(largest_int(65875))
print(largest_int(60))
print(largest_int(64))
print(largest_int(266))


# Example 1:
# Input: num = 1234
# Output: 3412
# Explanation: Swap the digit 3 with the digit 1, this results in the number 3214.
# Swap the digit 2 with the digit 4, this results in the number 3412.
# Note that there may be other sequences of swaps, but it can be shown that 3412 is the largest possible number.
# Also note that we may not swap the digit 4 with the digit 1 since they are of different parities.

# Example 2:
# Input: num = 65875
# Output: 87655
# Explanation: Swap the digit 8 with the digit 6, this results in the number 85675.
# Swap the first digit 5 with the digit 7, this results in the number 87655.
# Note that there may be other sequences of swaps, but it can be shown that 87655 is the largest possible number.
