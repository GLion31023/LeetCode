def sort_colors(nums: list[int]) -> None:
    i, s, e = 0, 0, len(nums) - 1

    while i <= e:
        if nums[i] == 0:
            nums[i], nums[s] = nums[s], nums[i]
            i += 1
            s += 1
        elif nums[i] == 2:
            nums[i], nums[e] = nums[e], nums[i]
            e -= 1
        else:
            i += 1


lst = [2, 0, 2, 1, 1, 0]
lst1 = [2, 0, 1]
lst2 = [1, 2, 0, 0, 1]
lst3 = [1, 1, 1, 0, 2, 2, 2, 0, 0, 0]
lst4 = [0, 0, 1, 0, 2, 2, 2, 0, 2, 2]
lst5 = [2, 1, 2]
lst6 = [1, 1, 2, 0, 2, 1, 0, 0, 2, 2]

sort_colors(lst)
sort_colors(lst1)
sort_colors(lst2)
sort_colors(lst3)
sort_colors(lst4)
sort_colors(lst5)
sort_colors(lst6)

print(lst)
print(lst1)
print(lst2)
print(lst3)
print(lst4)
print(lst5)
print(lst6)


# Example 1:
#
# Input: nums = [2,0,2,1,1,0]
# Output: [0,0,1,1,2,2]

# Example 2:
#
# Input: nums = [2,0,1]
# Output: [0,1,2]
