def zigzag_convert(s: str, num_rows: int) -> str:
    if num_rows == 1:
        return s

    rows = ["" for _ in range(num_rows)]

    r = 0
    d = 1

    for c in s:
        rows[r] += c
        if r == num_rows - 1 or r == 0 and d < 0:
            d *= -1
        r += d

    return "".join(rows)


print(zigzag_convert("PAYPALISHIRING", 3))
print(zigzag_convert("PAYPALISHIRING", 4))
print(zigzag_convert("ABC",1))
print(zigzag_convert("A",1))

# Example 1:
# Input: s = "PAYPALISHIRING", numRows = 3
# Output: "PAHNAPLSIIGYIR"

# Example 2:
# Input: s = "PAYPALISHIRING", numRows = 4
# Output: "PINALSIGYAHRPI"
# Explanation:
# P     I    N
# A   L S  I G
# Y A   H R
# P     I

# Example 3:
# Input: s = "A", numRows = 1
# Output: "A"
