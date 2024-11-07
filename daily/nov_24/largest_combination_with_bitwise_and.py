def largest_combination(candidates: list[int]) -> int:
    max_count = 0

    for bit in range(24):
        curr = 0
        for c in candidates:
            if c & (1 << bit):
                curr += 1
        max_count = max(max_count, curr)

    return max_count


print(largest_combination([16, 17, 71, 62, 12, 24, 14]))
print(largest_combination([8, 8]))
