def max_area(height: list[int]) -> int:
    left, right = 0, len(height) - 1
    area = 0

    while left < right:
        curr_area = (right - left) * min(height[left], height[right])
        area = max(curr_area, area)
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1

    return area


print(max_area([1, 8, 6, 2, 5, 4, 8, 3, 7]))
print(max_area([1, 1]))
print(max_area([1, 7, 2, 5, 4, 7, 3, 6]))
print(max_area([2, 2, 2]))
