def find_difference(nums1: list[int], nums2: list[int]) -> list[list[int]]:
    result = [[], []]
    seen1 = set(nums1)
    seen2 = set(nums2)

    for n in seen1:
        if n not in seen2:
            result[0].append(n)

    for n in seen2:
        if n not in seen1:
            result[1].append(n)

    return result


print(find_difference([1, 2, 3], nums2=[2, 4, 6]))
print(find_difference([1, 2, 3, 3], nums2=[1, 1, 2, 2]))
