def three_consecutive_odds(arr: list[int]) -> bool:
    one = two = False

    for n in arr:
        if n % 2 == 0:
            one = two = False
        elif one and two:
            return True
        elif one:
            two = True
        else:
            one = True

    return False


print(three_consecutive_odds([2, 6, 4, 1]))
print(three_consecutive_odds([1, 2, 34, 3, 4, 5, 7, 23, 12]))
