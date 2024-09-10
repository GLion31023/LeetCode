def pass_the_pillow(n: int, time: int) -> int:
    # mathematical approach to determine the position without iterating | O(1) time and space complexity
    cycle_len = 2 * (n - 1)

    time %= cycle_len

    if time < n:
        return time + 1
    else:
        return 2 * n - time - 1

    # dir_right = 1
    # i = 1
    #
    # while time > 0:
    #     if i == n:
    #         dir_right *= - 1
    #     elif i == 1:
    #         dir_right = 1
    #
    #     i += dir_right
    #     time -= 1
    #
    # return i


print(pass_the_pillow(n=4, time=5))
print(pass_the_pillow(n=3, time=2))
print(pass_the_pillow(n=18, time=38))
