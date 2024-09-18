def largest_number(nums: list[int]) -> str:
    array = list(map(str, nums))

    # without this we can to multiply by 9 (max len by constraint, and it will run faster, but it takes more memory
    max_len = max(len(s) for s in array)

    # Multiplying each number to the max length and then sorting as they are equal length
    # Example: 2 = 222 which then gets compared with 205205205, but we get that 205 should come behind 2
    array.sort(key=lambda x: x * max_len, reverse=True)

    if array[0] == "0":
        return "0"

    largest = ''.join(array)

    return largest


print(largest_number([10, 2]))
print(largest_number([0, 0]))
print(largest_number([3, 30, 34, 5, 9]))
print(largest_number([205, 23, 21, 25, 2]))
print(largest_number([432, 43243]))

# Example 1:
#
# Input: nums = [10,2]
# Output: "210"

# Example 2:
#
# Input: nums = [3,30,34,5,9]
# Output: "9534330"
