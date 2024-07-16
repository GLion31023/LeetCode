def unique_occurrences(arr: list[int]) -> bool:
    occur = {}

    for e in arr:
        if e in occur:
            occur[e] += 1
        else:
            occur[e] = 1

    seen = set()

    for v in occur.values():
        if v in seen:
            return False
        else:
            seen.add(v)

    return True


print(unique_occurrences([1, 2, 2, 1, 1, 3]))
print(unique_occurrences([1, 2]))
print(unique_occurrences([-3, 0, 1, -3, 1, 1, 1, -3, 10, 0]))
