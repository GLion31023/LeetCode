def pal_num(x: int) -> bool:
    if x < 0:
        return False

    s = str(x)

    return s == s[::-1]

    # left, right = 0, len(str(x)) - 1
    #
    # while left < right:
    #     if str(x)[left] != str(x)[right]:
    #         return False
    #     left += 1
    #     right -= 1
    #
    # return True


print(pal_num(x=121))
print(pal_num(x=-121))
print(pal_num(x=10))
