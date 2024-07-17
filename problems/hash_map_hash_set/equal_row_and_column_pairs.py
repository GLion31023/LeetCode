def equal_pairs(grid: list[list[int]]) -> int:
    equals = 0

    rows = [tuple(row) for row in grid]

    cols = [tuple(grid[i][j] for i in range(len(grid))) for j in range(len(grid))]

    rows_count = {}
    for row in rows:
        if row in rows_count:
            rows_count[row] += 1
        else:
            rows_count[row] = 1

    for col in cols:
        if col in rows_count:
            equals += rows_count[col]

    return equals


print(equal_pairs([[3, 2, 1], [1, 7, 6], [2, 7, 7]]))
print(equal_pairs([[3, 1, 2, 2], [1, 4, 4, 5], [2, 4, 2, 2], [2, 4, 2, 2]]))
print(equal_pairs([[3, 1, 2, 2], [1, 4, 4, 4], [2, 4, 2, 2], [2, 5, 2, 2]]))
print(equal_pairs([[13, 13], [13, 13]]))
