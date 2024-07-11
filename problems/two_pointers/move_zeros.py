def move_zeroes(nums: list[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    write = 0

    for i in range(len(nums)):
        if nums[i] != 0:
            nums[write] = nums[i]
            write += 1

    while write < len(nums):
        nums[write] = 0
        write += 1


arr = [0, 1, 0, 3, 12]
arr1 = [0]
move_zeroes(arr)
move_zeroes(arr1)
print(arr)
print(arr1)