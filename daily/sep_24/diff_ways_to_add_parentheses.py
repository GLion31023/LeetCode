def diff_ways_to_add(expression: str) -> list[int]:
    operations = {
        "+": lambda x, y: x + y,
        '-': lambda x, y: x - y,
        '*': lambda x, y: x * y
    }

    def compute(left, right):
        result = []

        for i in range(left, right + 1):
            sign = expression[i]
            if sign in operations:
                nums1 = compute(left, i - 1)
                nums2 = compute(i + 1, right)

                for n1 in nums1:
                    for n2 in nums2:
                        result.append(operations[sign](n1, n2))

        if not result:
            result.append(int(expression[left:right + 1]))

        return result

    return compute(0, len(expression) - 1)


print(diff_ways_to_add("2-1-1"))
print(diff_ways_to_add("2*3-4*5"))
print(diff_ways_to_add("11"))
print(diff_ways_to_add("10 + 5"))

# Example 1:
#
# Input: expression = "2-1-1"
# Output: [0,2]
# Explanation:
# ((2-1)-1) = 0
# (2-(1-1)) = 2

# Example 2:
#
# Input: expression = "2*3-4*5"
# Output: [-34,-14,-10,-10,10]
# Explanation:
# (2*(3-(4*5))) = -34
# ((2*3)-(4*5)) = -14
# ((2*(3-4))*5) = -10
# (2*((3-4)*5)) = -10
# (((2*3)-4)*5) = 10
