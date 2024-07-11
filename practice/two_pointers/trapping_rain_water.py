def trap(height: list[int]) -> int:
    if len(height) < 1:
        return 0

    left, right = 0, len(height) - 1
    max_left, max_right = height[left], height[right]
    trapped_water = 0

    while left < right:
        if max_left <= max_right:
            left += 1
            max_left = max(height[left], max_left)
            trapped_water += max_left - height[left]
        else:
            right -= 1
            max_right = max(height[right], max_right)
            trapped_water += max_right - height[right]

    return trapped_water


print(trap([0, 2, 0, 3, 1, 0, 1, 3, 2, 1]))
