from math import sqrt, floor


def my_sqrt(x: int) -> int:
    return floor(sqrt(x))
    # i = 0
    # while i * i <= x:
    #     i += 1
    # return i - 1


print(my_sqrt(4))
print(my_sqrt(8))
print(my_sqrt(16))
