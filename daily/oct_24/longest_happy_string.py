import heapq


def longest_string(a: int, b: int, c: int) -> str:
    counts = {'a': a, 'b': b, 'c': c}
    heap = [(-count, char) for char, count in counts.items()]
    heapq.heapify(heap)

    result = []

    while heap:
        count, char = heapq.heappop(heap)
        count = -count

        if len(result) >= 2 and result[-1] == result[-2] == char:
            if not heap:
                break

            next_count, next_char = heapq.heappop(heap)
            next_count = -next_count
            if next_count < 1:
                break
            result.append(next_char)
            if next_count > 1:
                heapq.heappush(heap, (-(next_count - 1), next_char))
            heapq.heappush(heap, (-count, char))
        else:
            if count < 1:
                break
            result.append(char)
            if count > 1:
                heapq.heappush(heap, (-(count - 1), char))

    return "".join(result)


print(longest_string(a=1, b=1, c=7))
print(longest_string(a=7, b=1, c=0))
print(longest_string(a=1, b=0, c=3))

# Example 1:
# Input: a = 1, b = 1, c = 7
# Output: "ccaccbcc"
# Explanation: "ccbccacc" would also be a correct answer.

# Example 2:
# Input: a = 7, b = 1, c = 0
# Output: "aabaa"
# Explanation: It is the only correct answer in this case.
